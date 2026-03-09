import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import copy
import os
from scipy.interpolate import interp1d

def plot_das_data(t_axis, x_axis, data, t_max = 60,
                  lb_perc = 1, up_perc = 99, lower_bound=False, upper_bound=False,
                  start_channel=None, end_channel=None, start_time=None, end_time=None,
                  save_fig=False, delays=None):
    if start_channel is not None and end_channel is not None:
        x_indices = np.where((x_axis >= start_channel) & (x_axis <= end_channel))[0]
        x_axis = x_axis[x_indices]
        data = data[:, x_indices]

    if start_time is not None and end_time is not None:
        start_index = np.searchsorted(t_axis, start_time)
        end_index = np.searchsorted(t_axis, end_time)
        t_axis = t_axis[start_index:end_index]
        data = data[start_index:end_index, :]

    y_lims = mdates.date2num(t_axis)
    if not lower_bound:
        lower_bound = np.percentile(data, lb_perc)
    if not upper_bound:
        upper_bound = np.percentile(data, up_perc)

    # Create the imshow plot
    fig, ax = plt.subplots(figsize=(12, 6))  # Adjust the figure size as needed
    plt.imshow(data[::-1,:], aspect='auto', vmin=lower_bound, vmax=upper_bound,
               extent=[min(x_axis), max(x_axis), 0, t_max],
               cmap='seismic')
    
    if delays is not None:        
        for i in range(0,len(t_axis)-np.int64(np.max(delays)),200):
            plt.plot(x_axis,t_axis[np.int64(delays)+i],'r--')

    plt.xlabel('Distance (m)', fontsize=24)
    plt.ylabel('Time (s)', fontsize=24)
    ax.tick_params(axis='both', which='major', labelsize=24)
    plt.gca().invert_yaxis()  # Invert the y-axis to have time increasing upwards
    plt.tight_layout()
    if save_fig:
        plt.savefig(save_fig)
#         plt.close()
    else:
        plt.show()
        
def plot_xcorr(xcorr, t_axis, x_axis=None, ax=None, figsize=(8, 10),
               cmap='seismic', vmax_use_max=False,
               fig_dir=None,
               fig_name=None,
               fontsize=30, tickfont=28,
               x_lim=None, y_lim=None,
               **plot_kwargs):
    if x_lim is None:
        x_lim = [-200, 200]
    if not ax:
        fig, ax = plt.subplots(figsize=figsize)
    x_origin_index = np.abs(x_axis).argmin()
    xcorr /= np.amax(xcorr[x_origin_index])
    vmax = plot_kwargs.get("vmax", np.percentile(np.absolute(xcorr), 99.5))

    start_x = 0
    end_x = xcorr.shape[0]

    if x_axis is not None:
        xcorr_to_plot = copy.deepcopy(xcorr)
    else:
        xcorr_to_plot = xcorr    
        
    plt.imshow(xcorr_to_plot.T, aspect="auto", vmax=vmax, vmin=-vmax, cmap=cmap,
               extent=[x_axis[0], x_axis[-1], t_axis[-1], t_axis[0]], interpolation='bicubic')
    

#     plt.xlabel("Channel #", fontsize=fontsize)
    plt.xlabel("Distance (m)", fontsize=fontsize)
    plt.ylabel("Time (s)", fontsize=fontsize)

    ax.tick_params(axis='both', which='major', labelsize=tickfont)

    plt.xlim(x_lim)
    if y_lim is not None:
        plt.ylim(y_lim)
    if fig_name and fig_dir:
        plt.tight_layout()
        fig_path = os.path.join(fig_dir, fig_name)
        plt.savefig(fig_path, bbox_inches='tight', dpi=300)
        print(f'{fig_path} has saved...')
#         plt.close()
    else:
        plt.show()    
        
def plot_fv_map(fv_map, freqs, vels, df, norm=True, vs=2400, fig_dir="Fig/", fig_name=None, ax=None, pclip=100, 
                fontsize=24, tickfont=20, **kwargs):

#     norm = True
    if norm:
        row_sums = np.amax(fv_map, axis=0)
        fv_map = fv_map / row_sums
    if not ax:
        fig, ax = plt.subplots(figsize=kwargs.get('figsize', (8,10)))

    pclip = 98
    vmax = np.percentile(np.abs(fv_map), pclip)
    vmin = np.percentile(np.abs(fv_map), 100-pclip)

    ax.imshow(fv_map, aspect="auto",
              extent=[freqs[0], freqs[-1], vels[0], vels[-1]],
              cmap="jet",
              vmax=vmax,
              vmin=vmin,
              alpha=0.7)
    if df:
        ax.scatter(df['freq'],df['vs']*vs,c='k',edgecolor=None,s=5,alpha=1)
    plt.xlim([np.min(freqs),np.max(freqs)])
    plt.ylim([np.min(vels),np.max(vels)])

    ax.grid()

    ax.set_xlabel("Frequency (Hz)", fontsize=fontsize)
    ax.set_ylabel("Phase velocity (m/s)", fontsize=fontsize)
    ax.tick_params(axis='both', which='major', labelsize=tickfont)
    plt.tight_layout()
    if fig_name:
        fig_path = os.path.join(fig_dir, fig_name)
        print(f'saving {fig_path}...')
        plt.savefig(f"{fig_path}", bbox_inches='tight', dpi=300)
#         plt.close()
    else:
        plt.show()

def compute_mac(mode_shape, x, ref_mode_shape, x_ref):
    """
    Interpolate reference mode shape onto x, then compute MAC between the two.

    Parameters:
    - mode_shape: np.ndarray, the mode shape to evaluate
    - x: np.ndarray, spatial coordinates of mode_shape
    - ref_mode_shape: np.ndarray, reference mode shape
    - x_ref: np.ndarray, spatial coordinates of ref_mode_shape

    Returns:
    - mac: float, Modal Assurance Criterion between mode_shape and interpolated ref_mode_shape
    """
    # Interpolate the reference mode shape onto x
    interp_func = interp1d(x_ref, ref_mode_shape, kind='linear', fill_value='extrapolate')
    ref_interp = interp_func(x)

    # Flatten and convert to numpy arrays (if needed)
    mode_shape = np.array(mode_shape).flatten()
    ref_interp = np.array(ref_interp).flatten()

    # Compute MAC
    numerator = np.abs(np.dot(mode_shape.conj(), ref_interp)) ** 2
    denominator = np.dot(mode_shape.conj(), mode_shape) * np.dot(ref_interp.conj(), ref_interp)

    mac = numerator / denominator if denominator != 0 else 0.0
    return mac

        
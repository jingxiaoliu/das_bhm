# Bridge Monitoring Using Existing Telecommunication Fiber-Optic Cables

This repository contains scripts and data used to generate figures for our study on bridge monitoring using Distributed Acoustic Sensing (DAS) on pre existing telecom or dark fiber (Telecom as Sensors).  

If you use this repository, please cite the associated paper and related works.

## Visualization

Final figure panels are provided in the `figs/` folder in PDF format.  [oai_citation:3‡GitHub](https://github.com/jingxiaoliu/das_bhm/tree/main/figs)  
Jupyter notebooks in the repository reproduce the main and extended figures.

## Hardware requirements

This implementation requires only a standard computer with enough RAM to support in memory operations for figure generation.

## Software requirements

OS Requirements  
This package is supported for Linux. It has been tested on Ubuntu Linux.

## Python Dependencies

This implementation mainly depends on the following Python packages.  [oai_citation:4‡GitHub](https://github.com/jingxiaoliu/das_bhm/blob/main/utils.py)
- numpy
- scipy
- matplotlib

Additional packages may be required depending on your environment and notebook execution.

## File List

### Data

Contains data files used to generate the main and extended figures.  [oai_citation:5‡GitHub](https://github.com/jingxiaoliu/das_bhm/tree/main/data)
- `data/fig1.npz`, `data/fig3.npz`, `data/fig4.npz`, `data/fig6.npz`
- `data/fig3f2.csv`, `data/supfig2.csv`
- `data/fig5_ms.npz`, `data/fig5a.npz`
- `data/extfig1.npz`, `data/extfig2.npz`, `data/extfig3.npz`, `data/extfig4.npz`, `data/extfig9.npz`
- `data/extfig1f1.npz`, `data/extfig1f2.csv`, `data/extfig2f1.npz`, `data/extfig2f2.csv`
- `data/extfig5_ms.npz`, `data/extfig5_ms.pkl`, `data/extfig5a.npz`
- `data/extfig6_ms.npz`, `data/extfig6a.npz`
- `data/extfig7_ms.npz`, `data/extfig7a.npz`

### Figs

Stores exported figure panels in PDF format.  [oai_citation:6‡GitHub](https://github.com/jingxiaoliu/das_bhm/tree/main/figs)
- Main figure panels, for example `fig1b.pdf`, `fig1c.pdf`, `fig4b.pdf`, `fig4c.pdf`, `fig6a.pdf`, `fig6b.pdf`, `fig6c.pdf`, `fig6d.pdf`
- Extended figure panels, for example `extfig1d.pdf`, `extfig1e.pdf`, `extfig1f.pdf`, `extfig2d.pdf`, `extfig2e.pdf`, `extfig2f.pdf`, `extfig3c.pdf`, `extfig3d.pdf`, `extfig5a.pdf`, `extfig6a.pdf`, `extfig6b.pdf`, `extfig7a.pdf`, `extfig7b.pdf`, `extfig9.pdf`
- Supplementary figure panel `supfig2.pdf`

### Scripts

Jupyter notebooks for reproducing figures.  [oai_citation:7‡GitHub](https://github.com/jingxiaoliu/das_bhm)
- `fig1.ipynb`
- `fig3_subfig2.ipynb`
- `fig4.ipynb`
- `fig5.ipynb`
- `fig6_extfig9.ipynb`
- `extfig1.ipynb`
- `extfig2.ipynb`
- `extfig3.ipynb`
- `extfig4.ipynb`
- `extfig5.ipynb`
- `extfig6.ipynb`
- `extfig7.ipynb`

### Modules

Python utilities used by the notebooks.  [oai_citation:8‡GitHub](https://github.com/jingxiaoliu/das_bhm)
- `utils.py`: plotting and processing helper functions used across figure notebooks

## Contact

Feel free to send any questions to:
- Jingxiao Liu (jingxiao@mit.edu)

# MagPhase
Phasing for metagenomics using PacBio long reads

Current Version (07/13/2021): MagPhase v1.0


## What is MagPhase?

MagPhase is for phasing of metagenomics data using long reads. 

MagPhase is a modified version of [IsoPhase](https://github.com/Magdoll/cDNA_Cupcake/wiki/IsoPhase:-Haplotyping-using-Iso-Seq-data) which was originally designed for isoform-level phasing of PacBio Iso-Seq (full-length transcript sequencing) data.

## Requirements & Installation

### Prerequisites

* Python (3.7+)
* minimap2

### Python-related libraries

* biopython
* bx-python
* scipy
* pysam
* pyvcf

### Installation using (Ana)Conda 

We recommend using [Anaconda](https://www.anaconda.com/products/individual) to set up your conda environment. Currently only Linux environments are supported.

(1) Install Conda Environment

```
export PATH=$PATH:<path_to_anaconda>/bin
conda -V
conda update conda
```

(2) Clone the Github repo and install using the yml script

```
git clone https://github.com/Magdoll/MagPhase.git
cd MagPhase
conda env create -f MagPhase.conda_env.yml
source activate MagPhase.env
```

(3) Once you have activated the virtual environment, you should see your prompt changing to something like this:

```
(MagPhase.env) $
```

## Example Usage

## Output Interpretation

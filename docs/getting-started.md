# Getting Started

## 1. Create and Activate Conda Environment

```powershell
conda create -n diem-validation python=3.11 -y
conda activate diem-validation
```

## 2. Install Dependencies

```powershell
conda install -c conda-forge polars openpyxl pyyaml mkdocs mkdocs-material -y
```

## 3. Launch Interactive Documentation (Recommended)

From repository root:

```powershell
.\documentation
```

Open `http://127.0.0.1:8000/`.

### Optional: install global `documentation` command in this conda env

```powershell
.\install-documentation-command.cmd
```

After that, with this env activated, you can run:

```powershell
documentation
```

## 4. Run Validation

Edit `configuration/validation_config.yaml`, then run:

```powershell
python validate.py
```

or

```powershell
.\validate.bat
```

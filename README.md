# StretchPro

**StretchPro** is a Windows desktop tool for rock art analysis, based on 
a PCA adptation and decorrelation stretching. It produces a set of 
complementary images that help visually distinguish faint or overlapping 
pigments that are hard to differentiate in the original photograph.

> This repository currently distributes the compiled **Windows executable**
> only. Source code will be released on paper acceptation. 

## Download

⬇️ [**Download StretchPro.exe**](https://github.com/ParrillaDigiarch/stretchpro/releases/latest/download/StretchPro.exe)

## Support

If you find StretchPro useful, consider supporting its development:

☕ [buymeacoffee.com/rparrilla](https://buymeacoffee.com/rparrilla)


## Workflow

1. **Select image** — choose the photo you want to process (any common
   image format: PNG, JPG, TIFF, BMP...).
2. **Select output path** — choose the folder where results will be saved.
3. **Select outputs to export** — tick which of the images below you want
   (all are ticked by default).
4. **Proceed** — StretchPro runs the full pipeline and saves the selected
   files into your chosen folder, named `{original_name}_{output}.png`
   (e.g. `cabra_whitebalance.png`).

Processing runs in the background, so the window stays responsive; progress
and any errors are shown in the log panel at the bottom.

## Outputs explained

| Output | What it shows |
|---|---|
| **Decorrelated MCA space** | The image projected onto its three MCA axes. This decorrelates the color channels (separating the dominant color trend from what varies independently), which is what makes faint pigment differences easier to isolate in the next steps. |
| **RGB inverse (white balanced)** | The final, corrected image — same as above, with automatic white balance applied. This is usually the main result you want to look at. |
| **High saturation index** | A grayscale mask highlighting strongly saturated regions — typically where a vivid pigment (e.g. a saturated red) is present. |
| **Low saturation index** | A grayscale mask highlighting muted, earthy-toned regions — typically associated with duller, brownish pigments. |
| **Low luma index** | A grayscale mask highlighting the darkest regions of the image — useful for spotting black pigment or deep shadow areas that may hide faint marks. |
| **Fusion image** | The corrected image blended to High sat index for an standard and easy to visualize image |
| **Transform matrix (`_matrix.txt`)** | The 3×3 MCA change-of-basis matrix used for that image, always exported regardless of your checkbox selection. Kept for reproducibility — it lets you document or re-derive exactly how a given result was produced. |


## Source code availability

The source code for StretchPro is not public yet. It will be released on publication
acceptance.

## Citation

If you use StretchPro in academic work, please cite it as:

> Parrilla, Rubén. (2026). *StretchPro* (version 0.1.0) [Software].
> https://github.com/ParrillaDigiarch/stretchpro


## License

StretchPro is provided free of charge for research and personal use. Please
credit the author and cite the software (see [Citation](#citation)) if it
contributes to published work.

# Anim·E

Anim·E - Anime-enhanced [DALL·E Mini](https://github.com/borisdayma/dalle-mini) (Craiyon)

## Play with the model

You can play with the model for free on Colab! [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cccntu/anim_e/blob/main/app.ipynb) (No Colab pro needed)


## Comparison

| Anim-E              |  Craiyon (formerly DALL-E mini) |
:-------------------------:|:-------------------------:
![](assets/images/hatsune_miku(Anim-E).png)  |  ![](assets/images/hatsune_miku(Craiyon).png)
![](assets/images/violet_evergarden(Anim-E).png)  |  ![](assets/images/violet_evergarden(Craiyon).png)
![](assets/images/vtuber_gawr_gura(Anim-E).png)  |  ![](assets/images/vtuber_gawr_gura(Craiyon).png)

## Credits

* Thanks [@borisdayma](https://github.com/borisdayma) for [DALL·E Mini](https://github.com/borisdayma/dalle-mini)
* Thanks [@kuprel](https://github.com/kuprel) for [min(DALL·E)](https://github.com/kuprel/min-dalle)
* Thanks [@patil-suraj](https://github.com/patil-suraj) for [vqgan-jax](https://github.com/patil-suraj/vqgan-jax)


## Model Card

This model is obtained by fine-tuning the VQGAN [weights](https://huggingface.co/dalle-mini/vqgan_imagenet_f16_16384) used by Craiyon, on a subset of Danbooru2017, [here](https://www.kaggle.com/datasets/mylesoneill/tagged-anime-illustrations)

The training only took about 9 hours on a single 3090.

## Releases

* [x] Flax inference code / reproduce the README images [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cccntu/anim_e/blob/main/notebooks/generate-readme-images.ipynb)

* [ ] Flax training code
* [ ] Fine-tuned [stable-diffusion](https://github.com/CompVis/stable-diffusion/blob/main/README.md) and code

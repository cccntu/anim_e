# %%
import requests
import torch
from min_dalle import MinDalle

VQGAN_URL = "https://huggingface.co/ttj/vqgan-anime/resolve/main/detoker.pt"


def download_detokenizer(self):
    if self.is_verbose:
        print("downloading detokenizer params")
    params = requests.get(VQGAN_URL)
    with open(self.detoker_params_path, "wb") as f:
        f.write(params.content)


MinDalle.download_detokenizer = download_detokenizer

# saves tokens for later use
old_image_grid_from_tokens = MinDalle.image_grid_from_tokens


def image_grid_from_tokens(
    self, image_tokens: torch.LongTensor, is_seamless: bool, is_verbose: bool = False
):
    self.generated_tokens = image_tokens.cpu().numpy()
    return old_image_grid_from_tokens(self, image_tokens, is_seamless, is_verbose)


MinDalle.image_grid_from_tokens = image_grid_from_tokens

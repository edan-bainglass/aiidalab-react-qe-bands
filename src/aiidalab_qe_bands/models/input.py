import typing as t

import pydantic as pdt


class BandsInput(pdt.BaseModel):
    model_config = pdt.ConfigDict(
        title="Band structure",
    )
    fat_bands: t.Annotated[
        bool,
        pdt.Field(
            title="Fat bands",
            description='"Fat bands" indicate a band structure plot that also visually represents the angular momentum contributions from specific atoms or orbitals to each energy band. The thickness of the each band represents the strength of these contributions, providing insight into the electronic structure.',
        ),
    ] = False

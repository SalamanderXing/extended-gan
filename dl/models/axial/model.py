from dl.base_lightning_modules.base_gan_model import GANLightning
from dl.base_lightning_modules.base_model import BaseRegressionModel

from argparse import Namespace

from ...components.conv3dmodel import CompactConv3DDiscriminator, Conv3DTemporalDiscriminator
from ...components.lstmconvmodel import ConvLSTMTemporalDiscriminator
from ...components.conv2dmodel import CompactFrameDiscriminator, FrameDiscriminator
from ...components.resnet3d import ResNet3DClassifier
from ...components.conv3dmodel import Conv3DFrameDiscriminator
from .modules import AxialGenerator

class Model(GANLightning):
    def __init__(self, params: Namespace):
        super().__init__(params)
        self.generator = AxialGenerator(params)
        self.temporal_discriminator = CompactConv3DDiscriminator(params)
        self.frame_discriminator = CompactFrameDiscriminator(params)

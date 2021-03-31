import torch
import torch.nn as nn

class Encoder(nn.Module):

    def __init__(self, img_shape, code_dim):
        super().__init__()

        self.conv_layers = nn.Sequential(
            nn.Conv2d(in_channels=img_shape[-1], out_channels=64, kernel_size=7, stride=1, padding=3),
            nn.LeakyReLU(),

            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(),

            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(),

            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(),
            
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU()
        )

        self.fc_layers = nn.Sequential(
            nn.Linear(in_features=4096, out_features=256),
            nn.LeakyReLU(),

            nn.Linear(in_features=256, out_features=256),
            nn.LeakyReLU(),

            nn.Linear(256, code_dim)
        )
        
        self.var_linear = nn.Linear(256, code_dim)

    def forward(self, x):
        batch_size = x.shape[0]

        x = self.conv_layers(x)
        x = x.view((batch_size, -1))
        
        self.fc_out = {}
        for i in range(len(self.fc_layers)):
            x = self.fc_layers[i](x)
            self.fc_out[i] = x
            
        logvar = self.var_linear(self.fc_out[3])
        return x, logvar
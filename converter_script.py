import torch
import torchvision.models as models

# Load a PyTorch model
model = models.resnet18(pretrained=True)
input_shape = (1, 3, 224, 224)  # input shape of the model

# Export the PyTorch model to ONNX format and save to file
output_file = "new_best.onnx"  # output file path and name
torch.onnx.export(model, torch.randn(input_shape), output_file,
                  opset_version=11,
                  input_names=["input"],
                  output_names=["output"],
                  dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}})


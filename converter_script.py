import torch
import argparse

parser = argparse.ArgumentParser(description='Convert PyTorch .pt model file to .onnx format.')
parser.add_argument('input_file', type=str, help='Path to input .pt model file')
parser.add_argument('output_file', type=str, help='Path to output .onnx model file')
args = parser.parse_args()

# Load the PyTorch model from the .pt file

model = torch.load('my_model.pt')
for module in model.modules():

# Set the input shape (if known)
input_shape = (1, 3, 224, 224)  # example input shape for image classification model
# Replace with your own input shape or set to None if unknown

# Export the model to ONNX format
dummy_input = torch.randn(input_shape, requires_grad=True)
torch.onnx.export(model, dummy_input, args.output_file, verbose=True)



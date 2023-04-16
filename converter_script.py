import torch
import onnx
import onnxruntime as ort
import torchvision.models as models
import numpy as np
def convert_pt_to_onnx(model_file, input_shape, output_file):
    # Load the PyTorch model
    model = torch.load(model_file)

    # Set the model to evaluation mode
    # Load a PyTorch model
    # Load a PyTorch model
    model = models.resnet18(pretrained=True)

    # Set the model to evaluation mode
    model.eval()

    # Create a dummy input tensor
    dummy_input = torch.randn(*input_shape)

    # Export the model to ONNX format
    torch.onnx.export(model, dummy_input, output_file, input_names=["input"], output_names=["output"])

    # Check that the ONNX model is valid
    onnx_model = onnx.load(output_file)
    onnx.checker.check_model(onnx_model)

    # Check that the ONNX model produces the same output as the PyTorch model
    ort_session = ort.InferenceSession(output_file)
    ort_inputs = {ort_session.get_inputs()[0].name: dummy_input.numpy()}
    ort_outputs = ort_session.run(None, ort_inputs)
    torch_outputs = model(dummy_input).detach().numpy()
    np.testing.assert_allclose(ort_outputs, torch_outputs, rtol=1e-03, atol=1e-05)


convert_pt_to_onnx("best.pt", (1, 3, 480, 640), "new_best.onnx")

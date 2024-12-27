from torch.utils.data import DataLoader, TensorDataset
import torch.nn as nn
import torch.optim as optim
import torch
import importlib

if hasattr(importlib, "invalidate_caches"):
	def invalidate_caches(cls=None):
		pass
	importlib.invalidate_caches = invalidate_caches

# GPU 디바이스 설정
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"사용 중인 디바이스: {device}")

# 간단한 PyTorch 모델 정의
class SimpleModel(nn.Module):
	def __init__(self):
		super(SimpleModel, self).__init__()
		self.layers = nn.Sequential(
			nn.Linear(10, 50),
			nn.ReLU(),
			nn.Linear(50, 20),
			nn.ReLU(),
			nn.Linear(20, 1)
		)

	def forward(self, x):
		return self.layers(x)

# 데이터 생성
def generate_data(num_samples=1000):
	x = torch.randn(num_samples, 10)
	y = x.sum(dim=1, keepdim=True) + torch.randn(num_samples, 1) * 2.0  # 잡음을 증가
	return x, y

# PyInstaller를 위한 함수 재정의
def script_method(fn, _rcb=None):
	return fn

def script(obj, optimize=True, _frames_up=0, _rcb=None):
	return obj

import torch.jit
torch.jit.script_method = script_method
torch.jit.script = script

if __name__ == "__main__":
	# 데이터 준비
	x_data, y_data = generate_data(num_samples=10000)  # 데이터 크기 증가
	dataset = TensorDataset(x_data, y_data)
	dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

	# 모델 준비
	model = SimpleModel().to(device)
	criterion = nn.MSELoss()  # 손실 함수
	optimizer = optim.Adam(model.parameters(), lr=0.001)  # 학습률 감소

	# 학습 루프
	num_epochs = 100
	for epoch in range(num_epochs):
		model.train()
		epoch_loss = 0

		for batch_x, batch_y in dataloader:
			batch_x, batch_y = batch_x.to(device), batch_y.to(device)

			optimizer.zero_grad()
			predictions = model(batch_x)
			loss = criterion(predictions, batch_y)
			loss.backward()
			optimizer.step()

			epoch_loss += loss.item()

		print(f"에포크 {epoch + 1}/{num_epochs}, 손실: {epoch_loss:.4f}")

	print("학습 완료!")

	# 테스트 데이터
	test_data = torch.randn(5, 10).to(device)
	model.eval()
	with torch.no_grad():
		test_predictions = model(test_data)

	print("\n테스트 결과:")
	for i, (input_vec, output) in enumerate(zip(test_data, test_predictions), 1):
		print(f"입력 {i}: {input_vec.tolist()} -> 출력: {output.item():.4f}")

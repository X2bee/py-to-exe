from cx_Freeze import setup, Executable

# 빌드 옵션
build_options = {
	"packages": [
		"torch"
	],
	"include_files": [
		(
			"/Users/sonseongjun/Library/Caches/pypoetry/virtualenvs/pytorch-pyinstaller-UNa3Va_d-py3.12/lib/python3.12/site-packages/torch/lib/libtorch_global_deps.dylib",
			"lib/torch/lib/libtorch_global_deps.dylib",
		),
	],
}

# 실행 파일 정의
executables = [
	Executable(
		"main.py",  # 메인 스크립트 파일명
		target_name="pytorch_app",  # 생성될 실행 파일명
	)
]

# setup 함수 정의
setup(
	name="PyTorch App",
	version="1.0",
	description="PyTorch Application Example",
	options={"build_exe": build_options},
	executables=executables,
)

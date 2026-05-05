from pathlib import Path

# range(256) → 0, 1, 2, ..., 255 숫자 시퀀스 생성하여 256 바이트 크기의 이진 파일 생성
content = bytes(range(256))

current_dir = Path(__file__).parent

# 'test_dummy.bin'이라는 이름으로 이진 파일 생성 및 내용 쓰기
with open(current_dir / "test_dummy.bin", "wb") as f:
    f.write(content)

print("테스트용 이진 파일 'test_dummy.bin'이 생성되었습니다.")

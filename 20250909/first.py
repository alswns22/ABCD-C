import pandas as pd
import numpy as np

# Excel 파일 읽기 (첫 번째 행을 헤더로 건너뛰기)
df = pd.read_excel(r"C:\ABCD-C\20250909\data.xlsx", header=1)

print("=== 원본 데이터 ===")
print(df)
print()

# 첫 번째 컬럼(Unnamed) 제거하고 이름 컬럼만 남기기
df = df.iloc[:, 1:]  # 첫 번째 컬럼 제거
df.columns = ['이름', '국어', '영어', '수학']  # 컬럼명 직접 지정

print("=== 정리된 데이터 ===")
print(df)
print()

# 과목 컬럼들
subject_cols = ['국어', '영어', '수학']

# 숫자로 변환
for col in subject_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 과목별 평균
print("=== 과목별 평균 ===")
for subject in subject_cols:
    avg = df[subject].mean()
    print(f"{subject}: {avg:.2f}점")
print()

# 학생별 평균
print("=== 학생별 평균 ===")
for idx, row in df.iterrows():
    name = row['이름']
    scores = row[subject_cols].dropna()  # NaN 제거
    if len(scores) > 0:
        avg = scores.mean()
        print(f"{name}: {avg:.2f}점")
print()

# 전체 통계
print("=== 전체 통계 ===")
all_scores = []
for col in subject_cols:
    all_scores.extend(df[col].dropna().tolist())

if len(all_scores) > 0:
    print(f"전체 평균: {np.mean(all_scores):.2f}점")
    print(f"최고 점수: {np.max(all_scores):.2f}점")
    print(f"최저 점수: {np.min(all_scores):.2f}점")
else:
    print("유효한 점수 데이터가 없습니다.")
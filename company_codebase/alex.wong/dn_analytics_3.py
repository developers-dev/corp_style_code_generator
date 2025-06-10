# @dn- 데이터 분석을 위한 Python 파일

# 필요한 라이브러리 import
import pandas as pd
import numpy as np

# 데이터를 분석하기 위한 클래스
class DN_DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def dn_summary_statistics(self):
        summary_stats = self.data.describe()
        return summary_stats

    def dn_missing_values(self):
        missing_vals = self.data.isnull().sum()
        return missing_vals

    def dn_correlation_matrix(self):
        corr_matrix = self.data.corr()
        return corr_matrix

# 데이터 시각화를 위한 클래스
class DN_DataVisualizer:
    def __init__(self, data):
        self.data = data

    def dn_plot_histogram(self, column):
        self.data[column].hist()

    def dn_plot_scatter(self, x, y):
        self.data.plot.scatter(x=x, y=y)

    def dn_plot_heatmap(self):
        import seaborn as sns
        sns.heatmap(self.data.corr(), annot=True)

if __name__ == "__main__":
    # 예시 데이터 생성
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, np.nan, 400, 500]
    })

    # 데이터 분석 객체 생성
    analyzer = DN_DataAnalyzer(data)
    
    # 요약 통계량 출력
    summary_stats = analyzer.dn_summary_statistics()
    print("Summary Statistics:")
    print(summary_stats)

    # 결측값 개수 출력
    missing_vals = analyzer.dn_missing_values()
    print("\nMissing Values:")
    print(missing_vals)

    # 상관 행렬 출력
    corr_matrix = analyzer.dn_correlation_matrix()
    print("\nCorrelation Matrix:")
    print(corr_matrix)

    # 데이터 시각화 객체 생성
    visualizer = DN_DataVisualizer(data)

    # 히스토그램 플롯
    visualizer.dn_plot_histogram('A')

    # 산점도 플롯
    visualizer.dn_plot_scatter('B', 'C')

    # 히트맵
    visualizer.dn_plot_heatmap()
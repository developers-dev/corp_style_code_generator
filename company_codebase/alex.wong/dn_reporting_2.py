# @dn- Reporting 기능을 담당하는 Python 파일

# 필요한 라이브러리 import
import pandas as pd
import matplotlib.pyplot as plt

# 데이터를 읽어오는 함수
def dn_load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# 데이터를 가공하는 함수
def dn_process_data(data):
    # 데이터 가공 로직 작성
    processed_data = data.groupby('category').sum()
    return processed_data

# 차트를 그리는 클래스
class DNReportingChart:
    def __init__(self, data):
        self.data = data

    def dn_bar_chart(self):
        plt.figure(figsize=(10, 6))
        plt.bar(self.data.index, self.data['value'])
        plt.xlabel('Category')
        plt.ylabel('Value')
        plt.title('Bar Chart')
        plt.show()

    def dn_pie_chart(self):
        plt.figure(figsize=(8, 8))
        plt.pie(self.data['value'], labels=self.data.index, autopct='%1.1f%%')
        plt.title('Pie Chart')
        plt.show()

# 메인 함수
def dn_main():
    file_path = 'data.csv'
    data = dn_load_data(file_path)
    processed_data = dn_process_data(data)

    chart = DNReportingChart(processed_data)
    chart.dn_bar_chart()
    chart.dn_pie_chart()

if __name__ == '__main__':
    dn_main()
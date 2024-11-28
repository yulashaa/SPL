import pandas as pd
import matplotlib.pyplot as plt
import mpld3

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.preprocess_data()

    def preprocess_data(self):
        # конвертація RGB-значень у кортежі
        self.data['RGB'] = self.data['RGB'].apply(
            lambda x: tuple(map(int, x.strip('rgb()').split(',')))
        )

    def get_extreme_values(self):
        extremes = {
            'HEX_min': self.data['HEX'].min(),
            'HEX_max': self.data['HEX'].max(),
            'RGB_min': self.data['RGB'].min(),
            'RGB_max': self.data['RGB'].max()
        }
        return extremes

    def plot_colors(self):
        colors = self.data['HEX']
        names = self.data['Name']

        plt.figure(figsize=(8, 6))
        plt.barh(names, [1] * len(names), color=colors)
        plt.xlabel('Color')
        plt.ylabel('Name')
        plt.title('Colors Visualization')
        plt.show()

    def advanced_visualizations(self):
        """Візуалізація кольорів у вигляді сітки."""
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_title("Color Grid")
        for i, (index, row) in enumerate(self.data.iterrows()):
            ax.add_patch(plt.Rectangle((i % 5, i // 5), 1, 1, color=row['HEX']))
        ax.set_xlim(0, 5)
        ax.set_ylim(0, len(self.data) // 5 + 1)
        ax.axis("off")
        plt.show()

    def multiple_subplots(self):
        """Створення кількох підграфіків із HEX і RGB значеннями."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        
        # HEX значення на гістограмі
        ax1.bar(self.data['Name'], range(len(self.data)), color=self.data['HEX'])
        ax1.set_title('HEX Colors')
        ax1.set_xticklabels(self.data['Name'], rotation=45, ha='right')

        # Значення RGB як діаграма розсіювання
        r, g, b = zip(*self.data['RGB'])
        ax2.scatter(r, g, c=self.data['HEX'], s=100)
        ax2.set_title('RGB Values')
        ax2.set_xlabel('Red')
        ax2.set_ylabel('Green')

        plt.tight_layout()
        plt.show()
        return fig

    def export_visualization(self, fig, filename, file_format='png'):
        """Експорт візуалізації у формат PNG, SVG або HTML."""
        if file_format in ['png', 'svg']:
            fig.savefig(f"{filename}.{file_format}", format=file_format)
        elif file_format == 'html':
            html = mpld3.fig_to_html(fig)
            with open(f"{filename}.html", 'w') as f:
                f.write(html)
        print(f"Visualization saved as {filename}.{file_format}")
        
    def run():
        file_path = '/Users/uliazapletnuk/Desktop/^_^/3kyrsik/python/lab8/color_srgb.csv'
        data_loader = DataLoader(file_path)

        extremes = data_loader.get_extreme_values()
        print("Екстремальні значення:", extremes)

        data_loader.plot_colors()

        data_loader.advanced_visualizations()

        fig = data_loader.multiple_subplots()
        data_loader.export_visualization(fig, 'color_chart', 'png')
        data_loader.export_visualization(fig, 'color_chart', 'html')
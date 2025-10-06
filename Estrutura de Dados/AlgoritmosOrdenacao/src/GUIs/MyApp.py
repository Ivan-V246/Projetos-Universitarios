# Cria de fato a interface da aplicacao
# Para futuras modificacao, e interessante implementar um esquema de navegacao usando QStackedWidget
from PySide6.QtWidgets import QMainWindow, QWidget, QCheckBox, QListWidget, QStyle, QFileDialog, QDialog, QProgressBar # Principais widgets
from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit, QListView, QAbstractItemView
from PySide6.QtGui import QFont, QIcon, QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QThread, Signal
from .widgets.smallWidgets import buttonMainMenu
from constants import ICON2_PATH, WINDOW_HEIGTH, WINDOW_WIDTH
from .Charts.generateCharts import MplCanvas
from matplotlib.ticker import ScalarFormatter
from datetime import datetime
import sys
import os
from teste_automatico.teste_automatico import AutoTeste
import asyncio

# Herda QMainWindow para ter acesso a alguns componentes da janela em si, como title e icon 
class MyWindow(QMainWindow):
    finished = Signal(float) # Sinal que terminou a execucao do algorítimo no caso de um teste de ordenacao
    
    def __init__(self):
        super().__init__()
        self.errorMessage = None # Gerencia a messagem de erro na leitura de dado, se ela deve ser exibida ou nao
        self.fileName = None # Gerencia o arquivo que será enviado para ordenar 
        self.algorithm = None # Gerencia o algorítmo escolhido para ordenação
        self.loading_dialog = None  # Gerencia o diálogo de carregamento
        self.autoTeste = None # Gerencia o teste automatico


        self.setWindowTitle("Algoritmos de Ordenação")
        self.setFixedSize(WINDOW_HEIGTH, WINDOW_WIDTH)
        self.setWindowIcon(QIcon(ICON2_PATH)) # Troca o icone da janela
        self.showMainMenu()  # Mostra a primeira janela


    # Renderiza o menu principal da aplicacao 
    def showMainMenu(self):
        CENTER = Qt.AlignmentFlag.AlignCenter # Cria um centralizacao 

        widget = QWidget() # Widget generico
        layout = QVBoxLayout() # Box vertical
        
        layout.setContentsMargins(0, 80, 0, 100) # Mergin no final e no inicio

        # Plota os gráficos usando os dados de ordenação
        button_view_graph = buttonMainMenu("Visualizar gráficos de desempenho")
        button_view_graph.clicked.connect(self.showCharts) # Adiciona funcao para esse botao
        
        # Reinicia os testes dos algoritmos de ordenação
        button_start_tests = buttonMainMenu("Realizar teste de algoritmo")
        button_start_tests.clicked.connect(self.startTest) # Adiciona funcao para esse botao
        
        # Compara Algoritmos
        button_compare_algorithms = buttonMainMenu("Comparar Algoritmos")
        button_compare_algorithms.clicked.connect(self.compareCharts) # Adiciona funcao para esse botao
        
        # Sai da aplicacao
        button_report = buttonMainMenu("Sair")
        button_report.clicked.connect(self.exitAplication) # Adiciona funcao para esse botao

        # Adiciona os botoes no layout
        layout.addWidget(button_view_graph, alignment=CENTER)
        layout.addWidget(button_start_tests, alignment=CENTER)
        layout.addWidget(button_compare_algorithms, alignment=CENTER)
        layout.addWidget(button_report, alignment=CENTER)
        
        widget.setLayout(layout) # Adiciona o layout no widget generico

        self.setCentralWidget(widget)  # Renderiza esse widget generico que foi criado 

    def showCharts(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # widget e layout da tela
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Seletor de Algoritmo para escolher quem vai ser usado
        label_select = QLabel("Selecione o algoritmo:")
        label_select.setFont(FONT)
    
        self.combo_algorithms = QComboBox()
        self.combo_algorithms.setFont(FONT)
        self.combo_algorithms.addItems(["Bubble Sort", "Selection Sort" , "Insertion Sort" , "Shell Sort", "Quick Sort", "Merge Sort", "Heap Sort"])

        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.clear
        self.canvas.axes.set_title("Desempenho do Algoritmo", fontsize=16)
        self.canvas.axes.set_xlabel("Quantidade de Nomes (Em milhares)")
        self.canvas.axes.set_ylabel("Tempo(ms)")
        self.canvas.figure.tight_layout()
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)

        self.canvas.draw()

        # Botão para plotar os gráficos do algoritmo selecionado
        button_plot = QPushButton("Gerar gráfico")
        button_plot.setFont(FONT)
        button_plot.setFixedSize(200, 40)
        button_plot.clicked.connect(self.updateChart)
    
        # Botão para voltar pro menu principal
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(200, 40)
        button_back.clicked.connect(self.showMainMenu)

        # Adiciona os botões e o gráfico no layout do widget
        layout.addWidget(label_select, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.combo_algorithms, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.canvas)
        layout.addWidget(button_plot, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(20, 0, 20, 40)

        widget.setLayout(layout)
        self.setCentralWidget(widget) # Renderiza na tela o widget criado

    def updateChart(self):
        algorithm = self.combo_algorithms.currentText() # Pega oque está selecionado no combo

        # Define as coordenadas de X que são sempre fixas
        x = [100, 250, 500]

        # Define as cores que serão usadas
        colors = {
            "Bubble Sort": "blue",
            "Selection Sort": "green",
            "Insertion Sort": "red",
            "Shell Sort": "cyan",
            "Quick Sort": "magenta",
            "Merge Sort": "yellow",
            "Heap Sort": "orange"
        }


        # Os valores de Y serão pegos dos dados gerados, os de agora são de exemplo
        # Altera o gráfico conforme o algoritmo selecionado
        if algorithm == "Bubble Sort":
            dados = self.canvas.getData("bubble_sort")
            y = [dados[100], dados[250], dados[500]]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (s)", fontsize=10, labelpad=8)
            self.canvas.axes.plot(x, y, marker='o', label=algorithm, color=colors["Bubble Sort"])
        
        if algorithm ==  "Selection Sort":
            dados = self.canvas.getData("selection_sort")
            y = [dados[100], dados[250], dados[500]]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (s)", fontsize=10, labelpad=8)
            self.canvas.axes.plot(x, y, marker='o', label=algorithm, color=colors["Selection Sort"])

        if algorithm == "Insertion Sort":
            dados = self.canvas.getData("insertion_sort")
            y = [dados[100], dados[250], dados[500]]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (s)", fontsize=10, labelpad=8)
            self.canvas.axes.plot(x, y, marker='o', label=algorithm, color=colors["Insertion Sort"])

        if algorithm ==  "Shell Sort":
            dados = self.canvas.getData("shell_sort")
            y = [dados[100]*1000, dados[250]*1000, dados[500]*1000]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (ms)", fontsize=10, labelpad=8)
            self.canvas.axes.plot(x, y, marker='o', label=algorithm, color=colors["Shell Sort"])

        if algorithm == "Quick Sort":
            dados = self.canvas.getData("quick_sort")
            y = [dados[100]*1000, dados[250]*1000, dados[500]*1000]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (ms)", fontsize=10, labelpad=8)
            self.canvas.axes.plot(x, y, marker='o', label=algorithm, color=colors["Quick Sort"])

        if algorithm == "Merge Sort":
            dados = self.canvas.getData("merge_sort")
            y = [dados[100]*1000, dados[250]*1000, dados[500]*1000]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (ms)", fontsize=10, labelpad=8)
            self.canvas.axes.plot(x, y, marker='o', label=algorithm, color=colors["Merge Sort"])
    
        if algorithm == "Heap Sort":
            dados = self.canvas.getData("heap_sort")
            y = [dados[100]*1000, dados[250]*1000, dados[500]*1000]
            self.canvas.axes.clear()
            self.canvas.axes.set_ylabel("Tempo (ms)", fontsize=10, labelpad=8)
            self.canvas.axes.plot(x, y, marker='o', label=algorithm, color=colors["Heap Sort"])
            

        # Atualiza o canvas
        self.canvas.axes.set_title(f"Desempenho: {algorithm}", fontsize=16)
        self.canvas.axes.set_xlabel("Quantidade de Nomes (Em milhares)", fontsize=10, labelpad=8)
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)
        self.canvas.axes.legend()
        self.canvas.figure.tight_layout()
        # val = datetime.now()  # Importa a data para ter nomes diferentes no arquivo do gráfico
        # self.canvas.figure.savefig(f"grafico{val}.png", dpi=300, bbox_inches="tight") # Salva o gráfico em PNG com qualidade melhorada
        self.canvas.draw()

    def compareCharts(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # widget e layout da tela
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Seletor de Algoritmo para escolher quem vai ser usado
        label_select = QLabel("Selecione os algoritmos:")
        label_select.setFont(FONT)
        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)
        self.view = QListView()
        self.view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        

        # Botão para plotar os gráficos do algoritmo selecionado
        button_plot = QPushButton("Gerar gráfico")
        button_plot.setFont(FONT)
        button_plot.setFixedSize(200, 40)
        button_plot.clicked.connect(self.updateMultiChart)
    
        # Botão para voltar pro menu principal
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(200, 40)
        button_back.clicked.connect(self.showMainMenu)

        # Canvas do matplotlib
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.clear
        self.canvas.axes.set_title("Desempenho do Algoritmo", fontsize=16)
        self.canvas.axes.set_xlabel("Quantidade de Nomes (Em milhares)")
        self.canvas.axes.set_ylabel("Tempo(ms)")
        self.canvas.figure.tight_layout()
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)

        self.canvas.draw()

        self.model = QStandardItemModel()
        lista = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Shell Sort", "Quick Sort", "Merge Sort", "Heap Sort"]
        for text in lista:
            item = QStandardItem(text)
            item.setCheckable(True)  # adiciona checkbox
            item.setCheckState(Qt.Unchecked)
            self.model.appendRow(item)
        
        # Adiciona os widgets ao layout
        layout.addWidget(label_select)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.view)
        layout.addWidget(self.canvas)
        layout.addWidget(button_plot, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(20, 20, 20, 20) # Margens


        self.view.setModel(self.model)
        self.model.dataChanged.connect(self.updateText)

        widget.setLayout(layout)
        self.setCentralWidget(widget) # Renderiza na tela o widget criado

    def updateMultiChart(self):
        x = [100, 250, 500]  # valores fixos de X

        # Define as cores que serão usadas para a plotagem dos gráficos
        colors = {
            "Bubble Sort": "blue",
            "Selection Sort": "green",
            "Insertion Sort": "red",
            "Shell Sort": "cyan",
            "Quick Sort": "magenta",
            "Merge Sort": "yellow",
            "Heap Sort": "orange"
        }


        selected = []
        for i in range(self.model.rowCount()):
            if self.model.item(i).checkState() == Qt.Checked:
                selected.append(self.model.item(i).text())

        if not selected:
            return  # Nenhum algoritmo selecionado
        
        self.canvas.axes.clear()
        alglog = ["Bubble Sort", "Insertion Sort", "Selection Sort"]

        test = False
        if any(item in selected for item in alglog):
            test = True
        for a in selected:
            dados = self.canvas.getData(a.lower().replace(" ", "_"))
            if test: 
                y = [dados[100], dados[250],dados[500]]
                self.canvas.axes.set_ylabel("Tempo (s)")
      
            else:
                y = [dados[100] * 1000, dados[250] * 1000, dados[500] * 1000]
                self.canvas.axes.set_ylabel("Tempo (ms)")

            self.canvas.axes.plot(x, y, marker='o', label=a, color=colors[a])

        # Atualiza o canvas
        self.canvas.axes.set_title(f"Desempenhos", fontsize=16)
        self.canvas.axes.set_xlabel("Quantidade de Nomes (Em milhares)", fontsize=10, labelpad=8)
        self.canvas.axes.grid(True, which="major", axis="y", linestyle="--", alpha=0.4)
        self.canvas.axes.margins(x=0.05, y=0.1)
        self.canvas.axes.yaxis.set_major_formatter(ScalarFormatter())
        self.canvas.axes.ticklabel_format(style='plain', axis='y')
        self.canvas.axes.legend()
        self.canvas.figure.tight_layout()
        # val = datetime.now()  # Importa a data para ter nomes diferentes no arquivo do gráfico
        # self.canvas.figure.savefig(f"grafico{val}.png", dpi=300, bbox_inches="tight") # Salva o gráfico em PNG com qualidade melhorada
        self.canvas.draw()



    def updateText(self):
        selected = []
        for i in range(self.model.rowCount()):
            if self.model.item(i).checkState() == Qt.Checked:
                selected.append(self.model.item(i).text())
        self.lineEdit.setText(", ".join(selected))

    def startTest(self):
        FONT = QFont("Arial")
        FONT.setPixelSize(25)

        # widget e layout da tela
        widget = QWidget()
        layout = QVBoxLayout()

        layout.setContentsMargins(20, 20, 20, 250) # Margens


        # Seletor de Algorítmo
        label_select_algorithm = QLabel("Selecione o algoritmo:")
        label_select_algorithm.setFont(FONT)
        label_select_algorithm.setFixedSize(560, 30)
        label_select_algorithm.setMargin(0)
        self.combo_algorithms = QComboBox()
        self.combo_algorithms.setFont(FONT)
        self.combo_algorithms.addItems(["Bubble Sort", "Selection Sort" , "Insertion Sort" , "Shell Sort", "Quick Sort", "Merge Sort", "Heap Sort"])
        self.combo_algorithms.setFixedSize(560, 40)

        # Seletor de arquivo para escolher quem vai ser usado
        self.label_select_file = QLabel("Nenhum Arquivo selecionado")
        self.label_select_file.setFont(FONT)
        self.label_select_file.setFixedSize(560, 30)
        self.label_select_file.setMargin(0)
        self.file_button = QPushButton("Selecionar arquivo")
        self.file_button.setFont(FONT)                # usa a mesma fonte do label
        self.file_button.setFixedSize(560, 60) 
        self.file_button.clicked.connect(self.selectFile)

        # Botao para confirmar os dados 
        button_find = QPushButton("Enviar")
        button_find.setFont(FONT)
        button_find.setFixedSize(560, 60)
        button_find.clicked.connect(self.showMessageDialog)

        # Botão para voltar pro menu principal
        button_back = QPushButton("Voltar")
        button_back.setFont(FONT)
        button_back.setFixedSize(560, 60)
        button_back.clicked.connect(self.showMainMenu)

        # Adiciona os Widgets no layout
        layout.addWidget(label_select_algorithm, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.combo_algorithms, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_select_file, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.file_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_find, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(button_back, alignment=Qt.AlignmentFlag.AlignCenter)

        widget.setLayout(layout)
        self.setCentralWidget(widget) # Renderiza o widget criado

    def selectFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self,"Escolha um arquivo", "", "Arquivos de texto(*.txt)")

        if file_path:
            self.fileName = file_path
            self.label_select_file.setText(f"Arquivo selecionado: {os.path.basename(file_path)}")
            
            
    def showMessageDialog(self):
        arquivo = self.fileName
        self.algorithm = self.combo_algorithms.currentText().lower().replace(" ", "") 
        algoritmo = self.algorithm   
        
        if arquivo:
            # Cria o fiálogo de carregamento
            self.loading_dialog = QDialog(self)
            self.loading_dialog.setWindowTitle("Processando")
            self.loading_dialog.setModal(True)

            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Barra de Carregamento
            label = QLabel("Executando algoritmo, aguarde...")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            progress = QProgressBar()
            progress.setRange(0,0)
            progress.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alinha barra de progresso

            # Adiciona os elementos no layout
            layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(progress, alignment=Qt.AlignmentFlag.AlignCenter)

            # Renderiza o diálogos
            self.loading_dialog.setLayout(layout)
            self.loading_dialog.setFixedSize(400, 100)
            self.loading_dialog.show() 

            # Cria e conecta o sinal
            self.autoTeste = AutoTeste(algoritmo, arquivo)
            self.autoTeste.finished.connect(self.end_exec)
            self.autoTeste.setParent(self) # Mantem a instancia ate o final da execuacao da tarefa
            self.autoTeste.start()  # Inicia a execução paralela
            print("Execução iniciada")
           
    # Metodo que ouve o final de autoTeste
    def end_exec(self, tempo_exec):
        print(f"Tempo de execução: {tempo_exec:.2f}s")
        self.autoTeste = None  # Libera referência depois de terminar
        if self.loading_dialog and self.loading_dialog.isVisible():
            self.loading_dialog.close()
            self.loading_dialog = None

        # Cria o diálogo que entregará o resultado ao usuário
        self.result = QDialog(self)
        self.result.setWindowTitle("Resultados")
        self.result.setModal(True)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Mensagens apresentadas ao usuário
        label_algoritmo = QLabel(f"Algoritmo escolhido: {self.algorithm}")
        label_algoritmo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_arquivo = QLabel(f"Arquivo escolhido: {os.path.basename(self.fileName)}")
        label_arquivo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_result = QLabel(f"Tempo Médio de Execução: {tempo_exec:.3f}s")
        label_result.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_obs = QLabel("Obs: Algorítmos com complexidade O(n²) são\nlimitados à testes com 25 mil itens")
        label_obs.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # adiciona os widgets ao layout
        layout.addWidget(label_algoritmo)
        layout.addWidget(label_arquivo)
        layout.addWidget(label_result)
        if self.algorithm in ["bubblesort", "selectionsort", "insertionsort"]:
            layout.addWidget(label_obs)
        # Renderiza o diálogos
        self.result.setLayout(layout)
        self.result.setFixedSize(400, 140)
        self.result.show()
          

    # Sai da aplicacao
    def exitAplication(self):
        sys.exit()
    
import random

class BoardGenerator:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.top_board = [[9]*self.width]*self.height
        self.board = [[] for j in range(self.height)]

    def generate(self):
        mines = 0
        for i in range(self.height):
            for _ in range(self.width):
                if  mines == self.mines:
                    pick = 0
                else:
                    pick = random.choice([-1, 0, 0, 0])
                self.board[i].append(pick)
                if pick == -1:
                    mines += 1
        random.shuffle(self.board)
        self._add_numbers()
        return self.board

    def _add_numbers(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == -1:
                    continue
                # vasen ylänurkka
                if i == 0 and j == 0:
                    mines = self.board[i][j:j+2].count(-1) + self.board[i+1][j:j+2].count(-1)
                # oikea ylänurkka
                elif i == 0 and j == self.width-1:
                    mines = self.board[i][j-1:j+1].count(-1) + self.board[i+1][j-1:j+1].count(-1)
                # vasen alanurkka
                elif i == self.height-1 and j == 0:
                    mines = self.board[i][j:j+2].count(-1) + self.board[i-1][j:j+2].count(-1)
                # oikea alanurkka
                elif i == self.height-1 and j == self.width-1:
                    mines = self.board[i][j-1:j+1].count(-1) + self.board[i-1][j-1:j+1].count(-1)
                # yläreuna
                elif i == 0:
                    mines = self.board[i][j-1:j+2].count(-1) + self.board[i+1][j-1:j+2].count(-1)
                # alareuna
                elif i == self.height-1:
                    mines = self.board[i][j-1:j+2].count(-1) + self.board[i-1][j-1:j+2].count(-1)
                # vasen reuna
                elif j == 0:
                    upper = self.board[i-1][j:j+2]
                    mid = self.board[i][j:j+2]
                    lower = self.board[i+1][j:j+2]
                    mines = upper.count(-1) + mid.count(-1) + lower.count(-1)
                # oikea reuna
                elif j == self.width-1:
                    upper = self.board[i-1][j-1:j+1]
                    mid = self.board[i][j-1:j+1]
                    lower = self.board[i+1][j-1:j+1]
                    mines = upper.count(-1) + mid.count(-1) + lower.count(-1)
                # muuten
                elif 0<i<self.height-1 and 0<j<self.width-1:
                    upper = self.board[i-1][j-1:j+2]
                    mid = self.board[i][j-1:j+2]
                    lower = self.board[i+1][j-1:j+2]
                    mines = upper.count(-1) + mid.count(-1) + lower.count(-1)
                self.board[i][j] = mines
    
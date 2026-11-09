class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            op = operations[i]
            
            try:
                newScore = int(op)
                if newScore >= -30000 and newScore <= 30000:
                    record.append(newScore)
            except ValueError:
                if op == "+":
                    prevScore1 = record[len(record) - 1]
                    prevScore2 = record[len(record) - 2]
                    newScore = prevScore1 + prevScore2
                    record.append(newScore)
                elif op == "D":
                    prevScore = record[len(record) - 1]
                    newScore = prevScore * 2
                    record.append(newScore)
                elif op== "C":
                    record.pop()

            print('record', i, record)
        
        return sum(record)


#include <stdio.h>

int main(){
    int row, column;
    scanf("%d %d", &row, &column);
    char maze[row][column];
    int money[row][column];
    for(int brick = 0; brick < column; ++brick){
        maze[0][brick] = '*';
        maze[row-1][brick] = '*';
    }
    for(int brick = 0; brick < row; ++brick){
        maze[brick][0] = '*';
        maze[brick][column-1] = '*';
    }
    for(int i = 1; i < row-1; ++i){
        for(int j = 1; j < column-1; ++j){
            maze[i][j] = ' ';
            money[i][j] = 0;
        }
    }
    char input;
    int startRow, startColumn, finishRow, finishColumn, inputRow, inputColumn, cost;
    do
    {
        scanf(" %c", &input);
        switch (input)
        {
        case 's':
            scanf("%d %d", &inputRow, &inputColumn);
            startRow = inputRow;
            startColumn = inputColumn;
            maze[inputRow][inputColumn] = 'O';
            break;
        case 'f':
            scanf("%d %d", &inputRow, &inputColumn);
            finishRow = inputRow;
            finishColumn = inputColumn;
            maze[inputRow][inputColumn] = ' ';
            break;
        case 'b':
            scanf("%d %d", &inputRow, &inputColumn);
            maze[inputRow][inputColumn] = '*';
            break;
        case '$':
            scanf("%d %d %d", &inputRow, &inputColumn, &cost);
            maze[inputRow][inputColumn] = '$';
            money[inputRow][inputColumn] = cost;
            break;
        case 'X':
            scanf("%d %d", &inputRow, &inputColumn);
            maze[inputRow][inputColumn] = 'X';
            break;
        default:
            break;
        }
    } while (input != 'e');
    for(int i = 0; i < row; ++i){//printing the maze.
        for(int j = 0; j < column; ++j){
            printf("%c", maze[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    char bin[2];
    int score = 0;
    int flag = 1;
    int checkForWinning = 0;
    int currentRow, currentColumn;
    currentRow = startRow;
    currentColumn = startColumn;
    int creature = 0;
    int q = 0;
    scanf("%2s", bin);// getting end's 'nd' side :))
    while(scanf(" %c", &input) != EOF && flag == 1){
        int newRow, newColumn;
        switch (input)
        {
        case 'u':
            newRow = currentRow-1;
            newColumn = currentColumn;
            break;
        case 'd':
            newRow = currentRow+1;
            newColumn = currentColumn;
            break;
        case 'r':
            newRow = currentRow;
            newColumn = currentColumn+1;
            break;
        case 'l':
            newRow = currentRow;
            newColumn = currentColumn -1;
            break;
        case 'q':
            flag = 0;
            checkForWinning = 0;
            q = 1;
            printf("YOU COULD NOT REACH THE FINAL POSITION :(\nGAME IS OVER!\n");
            break;
        default:
            break;
        }
        if(maze[newRow][newColumn] == '*'){
            printf("INVALID MOVE. TRY ANOTHER DIRECTION!\n");
            newRow = currentRow;
            newColumn = currentColumn;
        }
        else if(maze[newRow][newColumn] == 'X'){
            printf("YOU MET WITH THE ENEMY AND LOST THE GAME :(\nGAME IS OVER!\n");
            newRow = currentRow;
            newColumn = currentColumn;
            flag = 0;
            checkForWinning = 0;
            creature = 1;
        }
        else if(maze[newRow][newColumn] == '$'){
            printf("YOU GOT %d $.\n", money[newRow][newColumn]);
            score += money[newRow][newColumn];
            maze[currentRow][currentColumn] = ' ';
            maze[newRow][newColumn] = 'O';
            currentRow = newRow;
            currentColumn = newColumn;
        }
        else{
            maze[currentRow][currentColumn] = ' ';
            maze[newRow][newColumn] = 'O';
            currentRow =  newRow;
            currentColumn = newColumn;
        }
        if(currentRow == finishRow && currentColumn == finishColumn){
            flag = 0;
            checkForWinning = 1;
        }
        if(checkForWinning){
        printf("CONGRATS! YOU GOT %d BONUS:)\n", score);
        }
        for(int i = 0; i < row; ++i){//printing the maze.
        for(int j = 0; j < column; ++j){
            printf("%c", maze[i][j]);
        }
        printf("\n");
        }
        printf("\n");
        
    }

    if((creature != 1 && q != 1) && checkForWinning == 0){
        printf("YOU COULD NOT REACH THE FINAL POSITION :(\nGAME IS OVER!\n");
        for(int i = 0; i < row; ++i){//printing the maze.
        for(int j = 0; j < column; ++j){
            printf("%c", maze[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    }
    return 0;
}
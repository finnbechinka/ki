
- Trainieren Sie ein logistisches Regressionsmodell auf dem "Gaussian" Datensatz (linear separierbarer Datensatz, links-unten).  
  ![Alt text](Screenshot%202022-12-07%20at%2000-26-34%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
  - Fügen Sie dem Datensatz etwas Rauschen (Noise) hinzu und trainieren Sie erneut. Wie verhalten sich die Kosten? Warum?  
  ![Alt text](Screenshot%202022-12-07%20at%2000-26-50%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
  - Können Sie eine Überanpassung dieses Modells erreichen?  
  ![Alt text](Screenshot%202022-12-07%20at%2000-28-21%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
  - Trainieren Sie das Modell auf den anderen Datensätzen. Wie verhalten sich die Kosten? Warum?  
  ![Alt text](Screenshot%202022-12-07%20at%2000-29-13%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)  
  ![Alt text](Screenshot%202022-12-07%20at%2000-29-36%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)  
  ![Alt text](Screenshot%202022-12-07%20at%2000-29-45%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
- Trainieren Sie folgende MLPs auf dem kreisförmigen Datensatz (Circle) mehrmals mit jeweils den Aktivierungsfunktionen ReLU, tanh und Sigmoid:  
  - MLP mit einer versteckten Schicht mit zwei Neuronen. Erhöhen Sie schrittweise die Anzahl der Neuronen in der versteckten Schicht auf drei, vier und zuletzt auf fünf.  
    - 2 neuronen  
      - ReLU   
      ![Alt text](Screenshot%202022-12-07%20at%2000-04-14%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
      - tanh  
      ![Alt text](Screenshot%202022-12-07%20at%2000-05-21%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
      - Sigmoid  
      ![Alt text](Screenshot%202022-12-07%20at%2000-06-40%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
    - 3 neuronen  
      - ReLU   
      ![Alt text](Screenshot%202022-12-07%20at%2000-07-08%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
      - tanh  
      ![Alt text](Screenshot%202022-12-07%20at%2000-07-43%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
      - Sigmoid  
      ![Alt text](Screenshot%202022-12-07%20at%2000-08-38%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
    - 4 neuronen  
      - ReLU   
      ![Alt text](Screenshot%202022-12-07%20at%2000-09-02%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
      - tanh  
      ![Alt text](Screenshot%202022-12-07%20at%2000-09-36%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
      - Sigmoid  
      ![Alt text](Screenshot%202022-12-07%20at%2000-10-53%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
    - 5 neuronen  
      - ReLU   
      ![Alt text](Screenshot%202022-12-07%20at%2000-11-37%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
      - tanh  
      ![Alt text](Screenshot%202022-12-07%20at%2000-12-19%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
      - Sigmoid  
      ![Alt text](Screenshot%202022-12-07%20at%2000-13-19%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
  - MLP mit vier Schichten, mit jeweils 6 Zellen pro Schicht. 
    - ReLU  
    ![Alt text](Screenshot%202022-12-07%20at%2000-15-47%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
    - tanh  
    ![Alt text](Screenshot%202022-12-07%20at%2000-16-30%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
    - Sigmoid  
    ![Alt text](Screenshot%202022-12-07%20at%2000-17-43%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
- Trainieren Sie ein Netzwerk mit zwei versteckten Schichten mit jeweils 6 Neuronen einige Male auf dem spiralförmigen Datensatz (rechts unten). 
   ![Alt text](Screenshot%202022-12-07%20at%2000-37-39%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
  - Wie viele Epochen dauert das Training? Beobachten Sie Trainings- und Testkosten: liegt eine Überanpassung vor?  
  - Untersuchen Sie die Ausgaben der einzelnen Zellen, in dem Sie die Maus über die jeweilige Zelle bewegen. Bemerken Sie einen wesentlichen Unterschied in den Ausgaben der ersten Schicht im Vergleich zu der zweiten Schicht?  
  - Erhöhen Sie die Schichtanzahl auf drei, mit jeweils 7 Neuronen pro Schicht. Was können Sie über die Trainingszeit und Kosten sagen? Untersuchen und vergleichen Sie wieder die Ausgaben der Zellen in den drei Schichten.  
 ![Alt text](Screenshot%202022-12-07%20at%2000-40-23%20Tensorflow%20%E2%80%94%20Neural%20Network%20Playground.png)
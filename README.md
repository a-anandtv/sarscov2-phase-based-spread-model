# Phase based disease spread model for SARS-CoV-2 virus

A disease spread simulation based on the paper titled *“A mathematical model forsimulating the phase-basedtransmissibility of a novelcoronavirus” by Tian-Mu Chen et.al.* The simulation has been done in python and is using a system of ODEs(Ordinary Differential Equations) to solve for the disease spread trend from phase to phase. The simulation was done for a period of 120 days. The model correctly predicts the trend if a pre-fit assumption of the initial values are available. 

### Phase based model diagram

<p align="center">
  <img src="https://github.com/a-anandtv/sarscov2-phase-based-spread-model/blob/main/Resources/RPmodel.png" width="80%">
</p>

### Model simulation results (with pre-fit initial values)

*Simulation Results*

<p align="center">
  <img src="https://github.com/a-anandtv/sarscov2-phase-based-spread-model/blob/main/Resources/120days.png" width="80%">
</p>

*Simulation comparison with actual data*

<p align="center">
  <img src="https://github.com/a-anandtv/sarscov2-phase-based-spread-model/blob/main/Resources/realVsSimulated.png" width="80%">
</p>

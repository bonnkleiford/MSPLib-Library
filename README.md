# MSPLib-Library
<p align="center">
  <img width="500" alt="Screenshot 2021-05-20 at 16 19 59" src="https://user-images.githubusercontent.com/37835698/118995880-c6aecc80-b987-11eb-9b1d-094634e3b9d0.png">
</p>

### This version of the MSPLib Problems Library is still an **_INITIAL_** repository for synthetic problems.

# Welcome to MSPLib Problem Library!

We present `MSPLib`, a library of multistage stochastic programming problems to measure the computational performance of different implementations of stochastic dual dynamic programming (SDDP). The `MSPLib` contains large real-world instances as well as synthetic problems that are difficult to solve. We use the library to test prevailing implementations, including MSPPy, QUASAR, and SDDP.jl.

## Problem Instance Chart

### Multistage Stochastic Linear Programming Problems

#### Synthetic Problems:
<img width="1015" alt="Synthetic Problems (1-3)" src="https://github.com/bonnkleiford/MSPLib-Library/assets/37835698/0b7f340e-6ce5-4560-a738-4ef71e31f807">
<img width="1015" alt="Synthetic Problems (4-5)" src="https://github.com/bonnkleiford/MSPLib-Library/assets/37835698/a1995f0b-8191-4e0c-8453-5c489a4ccd19">
<img width="1015" alt="Synthetic Problems (6-8)" src="https://github.com/bonnkleiford/MSPLib-Library/assets/37835698/b28954c4-7b55-427f-a2b0-01e7d39c6805">
<img width="1015" alt="Synthetic Problems (9-10)" src="https://github.com/bonnkleiford/MSPLib-Library/assets/37835698/6097250b-e5a3-4678-b7cf-ec2831bfcd62">

#### Real-world Problems:
<img width="931" alt="Set of Real World Problems" src="https://github.com/bonnkleiford/MSPLib-Library/assets/37835698/159911be-c12e-4a61-a55e-d0d0fb16b289">

### HOW TO USE:
Each file in the `MSPLib` library follows the following convention:
<p align="center">
  <img width="643" alt="Screenshot 2023-09-12 at 21 44 23" src="https://github.com/bonnkleiford/MSPLib-Library/assets/37835698/2b0b4f56-8b8c-4a22-8d88-1bdec9432f3a">
</p>

If you want to obtain a particular file - problem model, lattice, first stage solution, bounds plot, etc - check the Problem Instance Chart above for the file name of the document following the convention.


<!---
#### Real-World Application Problems:
![MSLP 3](https://user-images.githubusercontent.com/37835698/183904468-9170049b-6ad4-4d2d-b18d-4a134cf7b8db.png)

<p align="center">
<img width="500" alt="Screenshot 2023-04-17 at 18 05 32" src="https://user-images.githubusercontent.com/37835698/232620924-795bffc4-7f48-4f93-b4e1-738bf0f7c10a.png">
</p>

The `MSPFormat` is our attempt to propose a standardized data structure format for SP and MSP problems. Similar to the other standardized data structure formats, the main objective of `MSPFormat` is easy accessibility and transfer of mathematical models and most especially for the users of the `MSPLIB` problem library users in simple, clear, and familiar manner. `MSPFormat` is serially compressed into the JavaScript Object Notation (JSON) format. JSON, an open-source standard file and data interchange format, is a common staple in data exchange in many computer languages. Consequently, as it is supported in various computer languages, parsing JSON files is achievable and straightforward.

The creation of `MSPFormat` arise with the following objectives in mind:
* To develop a format that can describe problems with multiple decision periods, myriad of state and control variables in a scalable manner;
* To create a data file format with an easy and familiar architecture to facilitate the verification of the mathematical model and the stochastic process;
* To devise an inclusive format to support diverse extensions of the classic stochastic programming, e.g., multi-stage, integrality, etc;
* To construct a standardized data format that separates the mathematical model from the description of the stochastic process, i.e., discretized samples, for MSP problems.

### Sample Problem
In order to understand better the structure of the `MSPFormat`, we present the Problem 1 - Instance 1 of the `MSPLib`, the simplified hydrothermal scheduling problem, and explain its corresponding two `MSPFormat` files in detail.

Given deterministic marginal cost of operation for a thermal- and a hydro-power generator, a generation quantity ($thermal_{t}$ and $hydro_{t}$, respectively) must be chosen to meet a known demand $D_t$ in each period $t$ of the planning horizon ($T = 1,2,3$). A reservoir, where the hydro-power generator draws water from, has a maximum capacity $C_t$ and we assume that it is full at the first planning period. There is also a possibility of spilling out water $spill_t$ by bypassing the turbine to prevent the water from over-topping the dam. The optimal strategy should minimize the expected cost of the operation - composed of fuels costs $c_f$ for the entire planning horizon. The main stochastic element of this problem comes from the water $inflow_t$. Inflows are the water that flows into the reservoir through rainfall or rivers. These inflows are uncertain, and are the cause of the main trade-off in hydro-thermal scheduling: the desire to use water now to generate cheap electricity, against the risk that future inflows will be low, leading to blackouts or expensive thermal generation.

##### Model
$$\begin{align}\min\ & \sum_{t=1}^T c_f *thermal_t  &&& \forall t \in T \\
\end{align}$$

$$\begin{align}s.t. \ & volume_t = volume_{t-1} - hydro_t - spill_t + inflow_t,  &&& \forall t \in T \\
& hydro_t + thermal_t = D_t,  &&& \forall t \in T \\
& volume_0 = 200, \\
& volume_t = C_t,  &&& \forall t \in T \\
\end{align}$$ 

```
{   "version":"MSMLP 1.1",
    "name":"Simple Hydrothermal Scheduling Problem - (Instance 1)",
    "maximize":false,
    "variables":[
        {"name": "volume",
         "stage":0,
         "obj":[0.0],
         "lb":[0.0],
         "ub":[200.0],
         "type":"CONTINUOUS"},
        {"name":"thermal_gen",
         "stage":0,
         "obj":[50.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"},
        {"name":"hydro_gen",
         "stage":0,
         "obj":[0.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"},
        {"name":"hydro_spill",
         "stage":0,
         "obj":[0.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"},
        {"name":"volume",
         "stage":1,
         "obj":[0.0],
         "lb":[0.0],
         "ub":[200.0],
         "type":"CONTINUOUS"},
        {"name":"thermal_gen",
         "stage":1,
         "obj":[100.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"}
        {"name":"hydro_gen",
         "stage":1,
         "obj":[0.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"},
        {"name":"hydro_spill",
         "stage":1,
         "obj":[0.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"},
        {"name":"volume",
         "stage":2,
         "obj":[0.0],
         "lb":[0.0],
         "ub":[200.0],
         "type":"CONTINUOUS"},
        {"name":"thermal_gen",
         "stage":2,
         "obj":[150.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"},
        {"name":"hydro_gen",
         "stage":2,
         "obj":[0.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"},
        {"name":"hydro_spill",
         "stage":2,
         "obj":[0.0],
         "lb":[0.0],
         "ub":["inf"],
         "type":"CONTINUOUS"}],
    "constraints":[
        {"name":"",
         "type":"EQ",
         "lhs":[
            {"name":"volume",
             "stage":0,
              "coefficient":[1.0]},
            {"name":"hydro_gen",
             "stage":0,
             "coefficient":[1.0]},
            {"name":"hydro_spill",
             "stage":0,
             "coefficient":[1.0]}],
        "rhs":[
            {"ADD":"inflow"},
            {"ADD":200.0},
            {"ADD":[0.0]}]},
        {"name":"",
         "type":"EQ",
         "lhs":[
            {"name":"hydro_gen",
             "stage":0,
              "coefficient":[1.0]},
            {"name":"thermal_gen",
             "stage":0,
             "coefficient":[1.0]}],
             "rhs":[150.0]},
        {"name":"",
         "type":"EQ",
         "lhs":[
            {"name":"volume",
             "stage":1,
             "coefficient":[1.0]},
            {"name":"volume",
             "stage":0,
             "coefficient":[-1.0]},
            {"name":"hydro_gen",
             "stage":1,
             "coefficient":[1.0]},
            {"name":"hydro_spill",
             "stage":1,
             "coefficient":[1.0]}],
        "rhs":[
            {"ADD":"inflow"},
            {"ADD":0.0}]},
        {"name":"",
         "type":"EQ",
         "lhs":[
            {"name":"hydro_gen",
             "stage":1,
             "coefficient":[1.0]},
            {"name":"thermal_gen",
             "stage":1,
             "coefficient":[1.0]}],
         "rhs":
            [150.0]},
        {"name":"",
         "type":"EQ",
         "lhs":[
            {"name":"volume",
             "stage":2,
             "coefficient":[1.0]},
            {"name":"volume",
             "stage":1,
             "coefficient":[-1.0]},
            {"name":"hydro_gen",
             "stage":2,
             "coefficient":[1.0]},
            {"name":"hydro_spill",
             "stage":2,
             "coefficient":[1.0]}],
         "rhs":[
            {"ADD":"inflow"},
            {"ADD":0.0}]},
        {"name":"",
         "type":"EQ",
         "lhs":[
            {"name":"hydro_gen",
             "stage":2,
             "coefficient":[1.0]},
            {"name":"thermal_gen",
             "stage":2,
             "coefficient":[1.0]}],
         "rhs":
            [150.0]}]}
```
-->

# Likelihood

We just looked at how the `scipy.optimize.curve_fit` function can be used to obtain the optimal parameters the agreement between some model and data.
To achieve this, the `curve_fit` function is maximising the likelihood of the model to the data, $\mathcal{L}\big[\mathbf{D} | M(\mathbf{X})\big]$.
For the specific case of Gaussian uncertainties, this may be called minimising the $\chi^2$-statistic.

The likelihood, given the model $M$ and a set of parameters $\mathbf{X}$, of the data $\mathbf{D}$ where these data are assumed to have Gaussian uncertainties can be found as,

$$ \ln\mathcal{L}\big[\mathbf{D} | M(\mathbf{X})\big] = -\frac{1}{2} \sum_n\Bigg({\bigg[\frac{y_n - M(\mathbf{X})}{\sigma_n}\bigg]^2 + \ln(2\pi\sigma_n)\Bigg)}, $$

where, $y_n$ is the $n$-th data value and $\sigma_n$ the associated uncertainty.

The likelihood is a probability distribution, that represents how well the parameter values reproduce the experimental data.
In the figure below, we show how the likelihood is affected by a change in $A$ and $\gamma$ for the Lorentzian modelling of QENS data discussed previously.
Note that the values of $x_0$ and $b$ are constrained to the optimal solutions found previously while $A$ and $\gamma$ were varied, the code to generate this figure can be found [here](./likelihood_code).

<center>
  <img src="https://github.com/arm61/trad_ml_methods/raw/main/likelihood_plot.png" alt="An example of a likelihood function, where $A$ and $\gamma$ are varied." class="bg-primary" width="500px">
</center<br>

It is clear that the likelihood is maximised at the optimised solutions for $A$ and $\gamma$ found previously, and indeed the shape of the likelihood appears to be Gaussian in nature.
These aspects will become important later in the course.

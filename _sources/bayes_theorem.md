# Bayes' theorem

The main idea behind all Bayesian modelling is that our prior knowledge about aspects of the model can, and should, inform our results.
This can take a variety of forms, it could be our understanding of certain parameter in our model or, as introduced previously, it may be our certainty about the model itself.
Bayes' theorem is generally written as follows,

$$ P(A|B) = \frac{P(B|A)P(A)}{P(B)}, $$

where, $P(A)$ and $P(B)$ are the independent probabilities of $A$ and $B$, and $P(A|B)$ is the probability of $A$ given $B$ is true and vice-versa for $P(B|A)$.
For our model selection problems, we will write Bayes' theorem with a slightly different phrasing,

$$ P(H_x|\mathbf{D}) = \frac{P(\mathbf{D}|H_x)P(H_x)}{P(\mathbf{D})}, $$

where, $H_x$ is our model (hypothesis), $P(\mathbf{D}|H_x)$ is the evidence for this model, $P(H_x)$ is the prior porbability for the model, $P(H_x|\mathbf{D})$ is the posterior probability, and $P(\mathbf{D})$ is the probability associated with the measured data.
This final object is a normalisation factor, and can be found as the sum of the evidence for every possible model.
However, it is typically not feasible to evaluate the evidence for **every** model, therefore we cannot truly quantify the posterior probability.

## The Bayes' factor

Despite this, we can still use this formulation for the comparison of different models for the same data.

$$\frac{P(H_x|\mathbf{D})}{P(H_y|\mathbf{D})} = \frac{P(\mathbf{D}|H_x)}{P(\mathbf{D}|H_y)} \times \frac{P(H_x)}{P(H_y)},$$

where the probabilities associated with the data only cancel out.
The ratio between the two models is known as the Bayes factor, $B_{xy}$, and offers insight into the relative evidence for the models.

The Bayes' factor is typically interpretated using the table below from the work of Kass and Raftery {cite}`kass_bayes_1995`.
Typically, for Bayesian model selection, we are comparing models with different numbers of parameters.
In this interpretation of the Bayes factor, the model $H_y$ has fewer parameters than $H_x$ and therefore for the latter model to be considered "better" is it necessary to have a substantially better evidence.
We can think of this as a quantification of Occam's razor.

| $2\ln(B_{xy})$ | Evidence against $H_y$ |
|---|---|
| $[0, 2)$ | Not worth a bare mention |
| $[2, 6)$ | Positive |
| $[6, 10)$ | Strong |
| $[10, \infty)$ | Very strong |


## Evidence

We have seen how we can compare our different models, but nothing has been said thus far about how the evidence is determined.
The evidence is the integral under the product of the likelihood, $\mathcal{L}(\mathbf{X}|H)$, and the parameter specific prior, $P(\mathbf{X}|H)$,

$$ P(\mathbf{D}|H) = \iint_{\mathbf{R}} \mathcal{L}(\mathbf{X}|H)P(\mathbf{X}|H)\; \text{d}^M\mathbf{X}, $$

where, $\mathbf{X}$ is a vector of length $M$ of the parameters that are varying in the model, $\mathbf{R}$ is a $2\times M$ matrix describing the range over which the integral should be evaluated.
As the shape of the likelihood function is not known *a priori*, however, the work of Sivia has involved assuming a Gaussian shape with some success {cite}`sivia_bayesian_1998,sivia_data_2005`.
To fully quantify the evidence it is necessary that sampling to evaluate this integral, but as $M$ increases, this will be more computationally intensive to achieve.
However, a variety of sampling algorithms have been developed to find the evidence for a given model {cite}`goodman_bayesian_2013`.
We will look at the nested sampling approach in this workshop. 

# 3_Body
A simple text-based real-time strategy game based around the 3-body problem

Introduction:

This project simulates the generation of 3-body star systems with astrophysically realistic properties. Each star is created using probabilistic mass sampling based on the Salpeter Initial Mass Function and assigned physical characteristics such as temperature, luminosity, spectral type, and luminosity class according to established stellar models. Planets are then generated within the habitable zone of a chosen host star, with parameters including mass, orbital radius, orbital period (calculated via Kepler’s Third Law), and estimated surface temperature based on stellar luminosity and orbital distance.

The system models stellar motion using vector values that represent relative movement toward or away from the host star, allowing for the calculation of relative velocities between stars. This setup provides a framework for simulating the dynamic environment of multi-star systems and their planets, which can be used as a foundation for further development of space exploration, colonization, or astrophysics-based simulations.

At the moment, the game is not playable. The following features are automated at launch.

  1. Star Generation:

  - Generates 3 stars by sampling their masses based on the Salpeter Initial Mass Function (a power-law distribution).
  - Calculates each star’s surface temperature, radius, and luminosity using approximate physical scaling relations.
  - Classifies the stars by spectral type and luminosity class according to their temperature and luminosity.
  - Assigns a random radial velocity vector between -1 and 1 to represent motion toward or away from the planet.

  2. Planet Generation:

  - Randomly selects one star as the host star.
  - Creates a planet orbiting the host star with:
      - A random mass between 0.5 and 3 Earth masses.
      - An orbital radius within the star’s habitable zone (estimated from stellar luminosity).
      - An orbital period calculated via Kepler’s Third Law.
      - An equilibrium surface temperature estimated by balancing absorbed and emitted radiation (blackbody model, including albedo).

  3. Outputs:

   - Prints the star system’s stars, the chosen host star, and the generated planet’s properties.

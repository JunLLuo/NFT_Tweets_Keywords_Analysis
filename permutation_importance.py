# MDA feature importance figure

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from eli5.sklearn import PermutationImportance
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


if __name__ == "__main__":
    # Generate synthetic data
    X, y = make_regression(n_samples=1000, n_features=50, noise=0.1, random_state=42)

    # Synthetic data just for demo
    keywords = [
        'AI', 'Blockchain', 'VR', 'AR', 'MachineLearning', 'DeepLearning',
        'NFT', 'Crypto', 'IoT', 'Quantum', 'Robotics', 'NeuralNetworks',
        'BigData', 'Cloud', 'Cybersecurity', 'DataScience', 'JavaScript',
        'Python', 'Ethereum', 'Bitcoin', 'Gaming', '3DPrinting', 'Drones',
        'AutonomousVehicles', 'Wearables', 'SaaS', '5G', 'EdgeComputing',
        'AugmentedReality', 'Serverless', 'QuantumComputing', 'RPA',
        'SmartCities', 'DevOps', 'UX', 'API', 'Web3.0', 'DataMining',
        'OpenSource', 'MixedReality', 'NanoTech', 'Holograms', 'Biotech',
        'GreenTech', 'MixedReality', 'SolarEnergy', 'VRGames', 'ARFilters',
        'Life', 'Hope'
    ]

    columns = keywords[:X.shape[1]]

    X_train = pd.DataFrame(X, columns=columns)
    y_train = y

    # Initialize and train a basic linear regression model for demo purpose
    model = LinearRegression()
    model.fit(X_train, y_train)

    perm = PermutationImportance(
        model, random_state=1, scoring="neg_mean_squared_error", n_iter=5
    ).fit(X_train, y_train)

    top_n = 30
    load_local = True

    df_results = pd.DataFrame(
        data=[r for r in perm.results_], columns=columns
    )

    feat_imps = df_results.mean().sort_values(ascending=False)

    df_results = df_results[feat_imps.index]

    df_results = df_results.iloc[:, list(range(0, top_n)) + list(range(-top_n, 0))]
    feat_imps = feat_imps[list(range(0, top_n)) + list(range(-top_n, 0))]

    y_layout = {
        "title_font_size": 6,
    }

    fig = px.box(
        df_results.melt(),
        x="variable",
        y="value",
        orientation="v",
        labels={"variable": "Feature word", "value": "Average feature importance"},
    )

    fig.add_trace(
        go.Scatter(
            x=feat_imps.index,
            y=feat_imps.values,
            mode="markers",
            marker=dict(color="red"),
            name="Mean",
        )
    )
    fig.update_xaxes(tickangle=300)

    fig.update_layout(
        font=dict(size=12, color="RebeccaPurple"),
        showlegend=False,
    )

    fig.show()

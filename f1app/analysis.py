import base64
import io
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sb
matplotlib.use('Agg')


class ChartGenerator():

    @staticmethod
    def first_ten():

        constructors = pd.read_csv(
            r"E:\f1project\f1app\data\constructors.csv", sep=',', encoding='utf-8')
        drivers = pd.read_csv(
            r"E:\f1project\f1app\data\drivers.csv", sep=';', encoding='utf-8')
        races = pd.read_csv(
            r"E:\f1project\f1app\data\races.csv", sep=';', encoding='utf-8')
        results = pd.read_csv(
            r"E:\f1project\f1app\data\results.csv", sep=';', encoding='latin-1')

        # merge datasets
        df = pd.merge(
            results, races[["raceId", "year", "name", "round"]], on="raceId", how="left")
        df = pd.merge(
            df, drivers[["driverId", "driverRef", "nationality"]], on="driverId", how="left")
        df = pd.merge(df, constructors[[
                      "constructorId", "name", "nationality"]], on="constructorId", how="left")

        # drop, rename, rearrange coloumns
        df.drop(["number", "position", "positionText", "laps", "fastestLap", "statusId",
                "resultId", "raceId", "driverId", "constructorId"], axis=1, inplace=True)
        df.rename(columns={"rank": "fastestLapRank", "name_x": "gpName", "nationality_x": "driverNationality",
                  "name_y": "constructorName", "nationality_y": "constructorNationality", "driverRef": "driver"}, inplace=True)
        df = df[["year", "gpName", "round", "driver", "constructorName", "grid", "positionOrder", "points", "time",
                 "milliseconds", "fastestLapRank", "fastestLapTime", "fastestLapSpeed", "driverNationality", "constructorNationality"]]

        # drop incomplete seasons
        df = df[df["year"] != 2021]
        df = df[df["year"] != 2022]

        # sort values
        df = df.sort_values(by=["year", "round", "positionOrder"], ascending=[
                            False, True, True])

        # reset index
        df.reset_index(drop=True, inplace=True)

        plt.rcParams["figure.figsize"] = 10, 6

        gp_winners = df.loc[df["positionOrder"] == 1].groupby("driver")[
            "positionOrder"].count().sort_values(ascending=False).to_frame().reset_index()

        sb.barplot(data=gp_winners, x="driver",
                   y="positionOrder", color="green", alpha=0.8)

        top_ten = gp_winners.head(10)

        fig = sb.barplot(data=top_ten, x="driver", y="positionOrder",
                         color="#636efa", alpha=0.8, linewidth=.8, edgecolor="black").figure

        plt.title("Top 10 Gp Winners")
        plt.xlabel("Drivers")
        plt.ylabel("Number of Wins")

        flike = io.BytesIO()
        fig.savefig(flike)
        b64 = base64.b64encode(flike.getvalue()).decode()

        return b64

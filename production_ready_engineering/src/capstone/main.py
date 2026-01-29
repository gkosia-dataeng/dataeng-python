import typer
import logging
from capstone.config.config import Config
from capstone.producer.producer import produce_data


app = typer.Typer()


@app.command()
def producer(ctx: typer.Context, num_of_events: int = typer.Option(20, help="Number of events to produce"))-> None:
    '''
        This command run the producer script to produce data under the folder in config.DATA_PATH
    '''
    logging.debug(f"Starting Producer process, producing {num_of_events} events")
    settings = ctx.obj
    produce_data(settings.DATA_PATH, num_of_events)

@app.command()
def etl(ctx: typer.Context)-> None:
    '''
        This command will trigger the ETL process 
        Data are ingested from config.DATA_PATH, validated and transformed and written in config.DB_PATH database
    '''
    logging.debug("Starting ETL process...")
    

@app.callback()
def main(ctx: typer.Context)-> None:

    settings = Config()
    logging.basicConfig(
         level=settings.LOG_LEVEL
        ,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logging.debug(f"Running with settings: {settings.__str__()}")

    ctx.obj = settings


if __name__ == "__main__":

    app()
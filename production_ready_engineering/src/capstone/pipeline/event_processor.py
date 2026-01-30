from capstone.models.events import Event
from pydantic import ValidationError
from pathlib import Path
import logging
from dataclasses import dataclass


@dataclass
class SourceFileData:
    valid_records: list[Event]
    invalid_records: list[str]

    @property
    def invalid_count(self) -> int:
        return len(self.invalid_records)


class Pipeline:
    
    def __init__(self, source_file: str | Path):
        self.source_file = source_file


    def run(self) -> None:
        records : list[str] = self.ingest()
        file_data : SourceFileData = self.validate_source_schema(records)


    def ingest(self) -> list[str]:

        try:
            return Path(self.source_file).read_text().splitlines()
        except FileNotFoundError:
            logging.error("Source data file not found at path %s", self.source_file)
            raise 
            


    def validate_source_schema(self, rows: list[str]) -> SourceFileData:
        
        valid_rows = []
        invalid_rows = []

        for row in rows:
            try:
                valid_rows.append(Event.model_validate_json(row))
            except ValidationError as v:
                logging.warning("Invalid row skipped: row=%s, reason=%s", row, v)
                invalid_rows.append(row)

        return SourceFileData(valid_records=valid_rows, invalid_records=invalid_rows)
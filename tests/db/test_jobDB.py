from __future__ import annotations

import asyncio

from pytest import mark
from pytest_asyncio import fixture

from chrishackaton.db.jobs.db import JobDB


@fixture
async def job_engine():
    await JobDB.make_engine("sqlite+aiosqlite:///:memory:")

    yield


@mark.asyncio
async def test_some_asyncio_code(job_engine: None):
    async with JobDB() as job_db:
        result = await job_db.list()

        assert not result

        result = await asyncio.gather(
            *(
                job_db.insert(f"JDL{i}", f"None{i}", f"originalJDL{i}")
                for i in range(100)
            )
        )

    async with JobDB() as job_db:
        result = await job_db.list()

        assert result
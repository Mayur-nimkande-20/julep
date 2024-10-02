# generated by datamodel-codegen:
#   filename:  openapi-0.4.0.yaml

from __future__ import annotations

from typing import Annotated, Any, Literal
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, StrictBool

from .Chat import ChatSettings
from .Docs import (
    EmbedQueryRequest,
    HybridDocSearchRequest,
    TextOnlyDocSearchRequest,
    VectorDocSearchRequest,
)
from .Tools import CreateToolRequest, NamedToolChoice


class CaseThen(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    case: Literal["_"] | str
    """
    The condition to evaluate
    """
    then: (
        EvaluateStep
        | ToolCallStep
        | PromptStep
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
        | ReturnStep
        | SleepStep
        | ErrorWorkflowStep
        | WaitForInputStep
    )
    """
    The steps to run if the condition is true
    """


class CaseThenUpdateItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    case: Literal["_"] | str
    """
    The condition to evaluate
    """
    then: (
        EvaluateStep
        | ToolCallStep
        | PromptStepUpdateItem
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
        | ReturnStep
        | SleepStep
        | ErrorWorkflowStep
        | WaitForInputStep
    )
    """
    The steps to run if the condition is true
    """


class Content(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    text: str
    """
    A valid jinja template.
    """
    type: Literal["text"] = "text"
    """
    The type (fixed to 'text')
    """


class ContentModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    image_url: ImageUrl
    """
    The image URL
    """
    type: Literal["image_url"] = "image_url"
    """
    The type (fixed to 'image_url')
    """


class ContentModel1(Content):
    pass


class ContentModel2(ContentModel):
    pass


class CreateTaskRequest(BaseModel):
    """
    Payload for creating a task
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    description: str = ""
    main: Annotated[
        list[
            EvaluateStep
            | ToolCallStep
            | PromptStep
            | GetStep
            | SetStep
            | LogStep
            | EmbedStep
            | SearchStep
            | YieldStep
            | ReturnStep
            | SleepStep
            | ErrorWorkflowStep
            | WaitForInputStep
            | IfElseWorkflowStep
            | SwitchStep
            | ForeachStep
            | ParallelStep
            | Main
        ],
        Field(min_length=1),
    ]
    """
    The entrypoint of the task.
    """
    input_schema: dict[str, Any] | None = None
    """
    The schema for the input to the task. `null` means all inputs are valid.
    """
    tools: list[TaskTool] = []
    """
    Tools defined specifically for this task not included in the Agent itself.
    """
    inherit_tools: StrictBool = True
    """
    Whether to inherit tools from the parent agent or not. Defaults to true.
    """
    metadata: dict[str, Any] | None = None


class EmbedStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["embed"], Field("embed", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    embed: EmbedQueryRequest
    """
    The text to embed
    """


class ErrorWorkflowStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["error"], Field("error", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    error: str
    """
    The error message
    """


class EvaluateStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["evaluate"], Field("evaluate", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    evaluate: dict[str, str]
    """
    The expression to evaluate
    """


class ForeachDo(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    in_: Annotated[str, Field(alias="in")]
    """
    The variable to iterate over.
    VALIDATION: Should NOT return more than 1000 elements.
    """
    do: (
        EvaluateStep
        | ToolCallStep
        | PromptStep
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
    )
    """
    The steps to run for each iteration
    """


class ForeachDoUpdateItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    in_: Annotated[str, Field(alias="in")]
    """
    The variable to iterate over.
    VALIDATION: Should NOT return more than 1000 elements.
    """
    do: (
        EvaluateStep
        | ToolCallStep
        | PromptStepUpdateItem
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
    )
    """
    The steps to run for each iteration
    """


class ForeachStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["foreach"], Field("foreach", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    foreach: ForeachDo
    """
    The steps to run for each iteration
    """


class ForeachStepUpdateItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: str | None = None
    """
    Discriminator property for BaseWorkflowStep.
    """
    foreach: ForeachDoUpdateItem
    """
    The steps to run for each iteration
    """


class GetStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[Literal["get"], Field("get", json_schema_extra={"readOnly": True})]
    """
    The kind of step
    """
    get: str
    """
    The key to get
    """


class IfElseWorkflowStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["if_else"], Field("if_else", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    if_: Annotated[str, Field(alias="if")]
    """
    The condition to evaluate
    """
    then: (
        EvaluateStep
        | ToolCallStep
        | PromptStep
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
        | ReturnStep
        | SleepStep
        | ErrorWorkflowStep
        | WaitForInputStep
    )
    """
    The steps to run if the condition is true
    """
    else_: Annotated[
        EvaluateStep
        | ToolCallStep
        | PromptStep
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
        | ReturnStep
        | SleepStep
        | ErrorWorkflowStep
        | WaitForInputStep
        | None,
        Field(None, alias="else"),
    ]
    """
    The steps to run if the condition is false
    """


class IfElseWorkflowStepUpdateItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: str | None = None
    """
    Discriminator property for BaseWorkflowStep.
    """
    if_: Annotated[str, Field(alias="if")]
    """
    The condition to evaluate
    """
    then: (
        EvaluateStep
        | ToolCallStep
        | PromptStepUpdateItem
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
        | ReturnStep
        | SleepStep
        | ErrorWorkflowStep
        | WaitForInputStep
    )
    """
    The steps to run if the condition is true
    """
    else_: Annotated[
        EvaluateStep
        | ToolCallStep
        | PromptStepUpdateItem
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
        | ReturnStep
        | SleepStep
        | ErrorWorkflowStep
        | WaitForInputStep
        | None,
        Field(None, alias="else"),
    ]
    """
    The steps to run if the condition is false
    """


class ImageUrl(BaseModel):
    """
    The image URL
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url: str
    """
    Image URL or base64 data url (e.g. `data:image/jpeg;base64,<the base64 encoded image>`)
    """
    detail: Literal["low", "high", "auto"] = "auto"
    """
    The detail level of the image
    """


class LogStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[Literal["log"], Field("log", json_schema_extra={"readOnly": True})]
    """
    The kind of step
    """
    log: str
    """
    The value to log
    """


class Main(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["map_reduce"], Field("map_reduce", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    over: str
    """
    The variable to iterate over
    """
    map: (
        EvaluateStep
        | ToolCallStep
        | PromptStep
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
    )
    """
    The steps to run for each iteration
    """
    reduce: str | None = None
    """
    The expression to reduce the results.
    If not provided, the results are collected and returned as a list.
    A special parameter named `results` is the accumulator and `_` is the current value.
    """
    initial: Any = []
    """
    The initial value of the reduce expression
    """
    parallelism: Annotated[int | None, Field(None, ge=1, le=100)]
    """
    Whether to run the reduce expression in parallel and how many items to run in each batch
    """


class MainModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: str | None = None
    """
    Discriminator property for BaseWorkflowStep.
    """
    over: str
    """
    The variable to iterate over
    """
    map: (
        EvaluateStep
        | ToolCallStep
        | PromptStepUpdateItem
        | GetStep
        | SetStep
        | LogStep
        | EmbedStep
        | SearchStep
        | YieldStep
    )
    """
    The steps to run for each iteration
    """
    reduce: str | None = None
    """
    The expression to reduce the results.
    If not provided, the results are collected and returned as a list.
    A special parameter named `results` is the accumulator and `_` is the current value.
    """
    initial: Any = []
    """
    The initial value of the reduce expression
    """
    parallelism: Annotated[int | None, Field(None, ge=1, le=100)]
    """
    Whether to run the reduce expression in parallel and how many items to run in each batch
    """


class ParallelStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["parallel"], Field("parallel", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    parallel: Annotated[
        list[
            EvaluateStep
            | ToolCallStep
            | PromptStep
            | GetStep
            | SetStep
            | LogStep
            | EmbedStep
            | SearchStep
            | YieldStep
        ],
        Field(max_length=100),
    ]
    """
    The steps to run in parallel. Max concurrency will depend on the platform.
    """


class ParallelStepUpdateItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: str | None = None
    """
    Discriminator property for BaseWorkflowStep.
    """
    parallel: Annotated[
        list[
            EvaluateStep
            | ToolCallStep
            | PromptStepUpdateItem
            | GetStep
            | SetStep
            | LogStep
            | EmbedStep
            | SearchStep
            | YieldStep
        ],
        Field(max_length=100),
    ]
    """
    The steps to run in parallel. Max concurrency will depend on the platform.
    """


class PatchTaskRequest(BaseModel):
    """
    Payload for patching a task
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    description: str = ""
    main: Annotated[
        list[
            EvaluateStep
            | ToolCallStep
            | PromptStepUpdateItem
            | GetStep
            | SetStep
            | LogStep
            | EmbedStep
            | SearchStep
            | YieldStep
            | ReturnStep
            | SleepStep
            | ErrorWorkflowStep
            | WaitForInputStep
            | IfElseWorkflowStepUpdateItem
            | SwitchStepUpdateItem
            | ForeachStepUpdateItem
            | ParallelStepUpdateItem
            | MainModel
        ]
        | None,
        Field(None, min_length=1),
    ]
    """
    The entrypoint of the task.
    """
    input_schema: dict[str, Any] | None = None
    """
    The schema for the input to the task. `null` means all inputs are valid.
    """
    tools: list[TaskTool] = []
    """
    Tools defined specifically for this task not included in the Agent itself.
    """
    inherit_tools: StrictBool = True
    """
    Whether to inherit tools from the parent agent or not. Defaults to true.
    """
    metadata: dict[str, Any] | None = None


class PromptItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    role: Literal[
        "user",
        "assistant",
        "system",
        "function",
        "function_response",
        "function_call",
        "auto",
    ]
    """
    The role of the message
    """
    content: list[str] | list[Content | ContentModel] | str
    """
    The content parts of the message
    """
    name: str | None = None
    """
    Name
    """
    continue_: Annotated[StrictBool | None, Field(None, alias="continue")]
    """
    Whether to continue this message or return a new one
    """


class PromptStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["prompt"], Field("prompt", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    prompt: list[PromptItem] | str
    """
    The prompt to run
    """
    tools: Literal["all"] | list[ToolRef | CreateToolRequest] = []
    """
    The tools to use for the prompt
    """
    tool_choice: Literal["auto", "none"] | NamedToolChoice | None = None
    """
    The tool choice for the prompt
    """
    settings: ChatSettings | None = None
    """
    Settings for the prompt
    """
    unwrap: StrictBool = False
    """
    Whether to unwrap the output of the prompt step, equivalent to `response.choices[0].message.content`
    """
    forward_tool_results: StrictBool | None = None
    """
    Whether to forward the tool results to the model when available.
    "true" => always forward
    "false" => never forward
    null => forward if applicable (default)

    If a tool call is made, the tool's output will be used as the model's input.
    If a tool call is not made, the model's output will be used as the next step's input.
    """


class PromptStepUpdateItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: str | None = None
    """
    Discriminator property for BaseWorkflowStep.
    """
    prompt: list[PromptItem] | str
    """
    The prompt to run
    """
    tools: Literal["all"] | list[ToolRefUpdateItem | CreateToolRequest] = []
    """
    The tools to use for the prompt
    """
    tool_choice: Literal["auto", "none"] | NamedToolChoice | None = None
    """
    The tool choice for the prompt
    """
    settings: ChatSettings | None = None
    """
    Settings for the prompt
    """
    unwrap: StrictBool = False
    """
    Whether to unwrap the output of the prompt step, equivalent to `response.choices[0].message.content`
    """
    forward_tool_results: StrictBool | None = None
    """
    Whether to forward the tool results to the model when available.
    "true" => always forward
    "false" => never forward
    null => forward if applicable (default)

    If a tool call is made, the tool's output will be used as the model's input.
    If a tool call is not made, the model's output will be used as the next step's input.
    """


class ReturnStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["return"], Field("return", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    return_: Annotated[dict[str, str], Field(alias="return")]
    """
    The value to return
    """


class SearchStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["search"], Field("search", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    search: VectorDocSearchRequest | TextOnlyDocSearchRequest | HybridDocSearchRequest
    """
    The search query
    """


class SetStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[Literal["set"], Field("set", json_schema_extra={"readOnly": True})]
    """
    The kind of step
    """
    set: dict[str, str]
    """
    The value to set
    """


class SleepFor(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    seconds: Annotated[int, Field(0, ge=0, le=60)]
    """
    The number of seconds to sleep for
    """
    minutes: Annotated[int, Field(0, ge=0, le=60)]
    """
    The number of minutes to sleep for
    """
    hours: Annotated[int, Field(0, ge=0, le=24)]
    """
    The number of hours to sleep for
    """
    days: Annotated[int, Field(0, ge=0, le=30)]
    """
    The number of days to sleep for
    """


class SleepStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["sleep"], Field("sleep", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    sleep: SleepFor
    """
    The duration to sleep for (max 31 days)
    """


class SwitchStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["switch"], Field("switch", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    switch: Annotated[list[CaseThen], Field(min_length=1)]
    """
    The cond tree
    """


class SwitchStepUpdateItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: str | None = None
    """
    Discriminator property for BaseWorkflowStep.
    """
    switch: Annotated[list[CaseThenUpdateItem], Field(min_length=1)]
    """
    The cond tree
    """


class Task(BaseModel):
    """
    Object describing a Task
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: str
    description: str = ""
    main: Annotated[
        list[
            EvaluateStep
            | ToolCallStep
            | PromptStep
            | GetStep
            | SetStep
            | LogStep
            | EmbedStep
            | SearchStep
            | YieldStep
            | ReturnStep
            | SleepStep
            | ErrorWorkflowStep
            | WaitForInputStep
            | IfElseWorkflowStep
            | SwitchStep
            | ForeachStep
            | ParallelStep
            | Main
        ],
        Field(min_length=1),
    ]
    """
    The entrypoint of the task.
    """
    input_schema: dict[str, Any] | None = None
    """
    The schema for the input to the task. `null` means all inputs are valid.
    """
    tools: list[TaskTool] = []
    """
    Tools defined specifically for this task not included in the Agent itself.
    """
    inherit_tools: StrictBool = True
    """
    Whether to inherit tools from the parent agent or not. Defaults to true.
    """
    id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    updated_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was updated as UTC date-time
    """
    metadata: dict[str, Any] | None = None


class TaskTool(CreateToolRequest):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    inherited: Annotated[StrictBool, Field(False, json_schema_extra={"readOnly": True})]
    """
    Read-only: Whether the tool was inherited or not. Only applies within tasks.
    """


class ToolCallStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["tool_call"], Field("tool_call", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    tool: Annotated[str, Field(max_length=40, pattern="^[^\\W0-9]\\w*$")]
    """
    The tool to run
    """
    arguments: dict[str, str] | Literal["_"] = "_"
    """
    The input parameters for the tool (defaults to last step output)
    """


class ToolRef(BaseModel):
    """
    Reference to a tool
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    ref: ToolRefById | ToolRefByName


class ToolRefById(BaseModel):
    """
    Reference to a tool by id
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    id: UUID | None = None


class ToolRefByName(BaseModel):
    """
    Reference to a tool by name
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    name: Annotated[str | None, Field(None, max_length=40, pattern="^[^\\W0-9]\\w*$")]
    """
    Valid python identifier names
    """


class ToolRefUpdateItem(BaseModel):
    """
    Reference to a tool
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )


class UpdateTaskRequest(BaseModel):
    """
    Payload for updating a task
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    description: str = ""
    main: Annotated[
        list[
            EvaluateStep
            | ToolCallStep
            | PromptStep
            | GetStep
            | SetStep
            | LogStep
            | EmbedStep
            | SearchStep
            | YieldStep
            | ReturnStep
            | SleepStep
            | ErrorWorkflowStep
            | WaitForInputStep
            | IfElseWorkflowStep
            | SwitchStep
            | ForeachStep
            | ParallelStep
            | Main
        ],
        Field(min_length=1),
    ]
    """
    The entrypoint of the task.
    """
    input_schema: dict[str, Any] | None = None
    """
    The schema for the input to the task. `null` means all inputs are valid.
    """
    tools: list[TaskTool] = []
    """
    Tools defined specifically for this task not included in the Agent itself.
    """
    inherit_tools: StrictBool = True
    """
    Whether to inherit tools from the parent agent or not. Defaults to true.
    """
    metadata: dict[str, Any] | None = None


class WaitForInputInfo(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    info: dict[str, str]
    """
    Any additional info or data
    """


class WaitForInputStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["wait_for_input"],
        Field("wait_for_input", json_schema_extra={"readOnly": True}),
    ]
    """
    The kind of step
    """
    wait_for_input: WaitForInputInfo
    """
    Any additional info or data
    """


class YieldStep(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    kind_: Annotated[
        Literal["yield"], Field("yield", json_schema_extra={"readOnly": True})
    ]
    """
    The kind of step
    """
    workflow: str
    """
    The subworkflow to run.
    VALIDATION: Should resolve to a defined subworkflow.
    """
    arguments: dict[str, str] | Literal["_"] = "_"
    """
    The input parameters for the subworkflow (defaults to last step output)
    """
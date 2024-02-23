# Julep in a nutshell

{% hint style="info" %}
At its core, Julep is a platform for creating and deploying agents[^1] powered by LAME[^2].

Read more about about agents [here](../concepts/what-are-agents.md) and LAME [here](../concepts/what-is-lame.md).
{% endhint %}

### Agents Platform

Julep is kind of like a superpowered version of the Assistants' API allows you to create _stateful actors_ from a specification containing _instructions_ and, _tools_. Also called agents.

These agents can be [chatted with](#user-content-fn-3)[^3] or invoked to [perform tasks](#user-content-fn-4)[^4]. Julep orchestrates its entire lifecycle of running prompts, calling APIs, saving state, managing context, recovering from failures, waiting for tool results and then coming up with the final output.

This abstraction lets you focus on writing prompts for planning and the tools needed by the agent. The heavylifting of the orchestration and memory management is handled by Julep.

### Large Agent Model Executor (LAME)



{% hint style="success" %}
In order to make this work, we trained a foundation model to execute these specifications natively that we call LAME.&#x20;
{% endhint %}

Model trained for this stuff.

[^1]: An agent is a prgram that uses foundation models to carry out complex tasks autonomously.

[^2]: Large Agent Model Execution

[^3]: You can chat with agents inside `Sessions` created using the API.

[^4]: `Tasks` are long-lived executions in which agents can use tools to achieve complex goals.
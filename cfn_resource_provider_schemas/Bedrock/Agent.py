SCHEMA = {
  "typeName" : "AWS::Bedrock::Agent",
  "description" : "Definition of AWS::Bedrock::Agent Resource Type",
  "definitions" : {
    "APISchema" : {
      "description" : "Contains information about the API Schema for the Action Group",
      "oneOf" : [ {
        "type" : "object",
        "title" : "S3",
        "properties" : {
          "S3" : {
            "$ref" : "#/definitions/S3Identifier"
          }
        },
        "required" : [ "S3" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "Payload",
        "properties" : {
          "Payload" : {
            "type" : "string",
            "description" : "String OpenAPI Payload"
          }
        },
        "required" : [ "Payload" ],
        "additionalProperties" : False
      } ]
    },
    "ActionGroupExecutor" : {
      "description" : "Type of Executors for an Action Group",
      "oneOf" : [ {
        "type" : "object",
        "title" : "Lambda",
        "properties" : {
          "Lambda" : {
            "type" : "string",
            "maxLength" : 2048,
            "pattern" : "^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\\d{1}:\\d{12}:function:[a-zA-Z0-9-_\\.]+(:(\\$LATEST|[a-zA-Z0-9-_]+))?$",
            "description" : "ARN of a Lambda."
          }
        },
        "required" : [ "Lambda" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "CustomControl",
        "properties" : {
          "CustomControl" : {
            "$ref" : "#/definitions/CustomControlMethod"
          }
        },
        "required" : [ "CustomControl" ],
        "additionalProperties" : False
      } ]
    },
    "ActionGroupSignature" : {
      "type" : "string",
      "description" : "Action Group Signature for a BuiltIn Action",
      "enum" : [ "AMAZON.UserInput", "AMAZON.CodeInterpreter" ]
    },
    "ActionGroupState" : {
      "type" : "string",
      "description" : "State of the action group",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "AdditionalModelRequestFields" : {
      "type" : "object",
      "description" : "Additional Model Request Fields for Prompt Configuration"
    },
    "AgentActionGroup" : {
      "type" : "object",
      "description" : "Contains the information of an Agent Action Group",
      "properties" : {
        "ActionGroupName" : {
          "type" : "string",
          "pattern" : "^([0-9a-zA-Z][_-]?){1,100}$",
          "description" : "Name of the action group"
        },
        "Description" : {
          "type" : "string",
          "maxLength" : 200,
          "minLength" : 1,
          "description" : "Description of action group"
        },
        "ParentActionGroupSignature" : {
          "$ref" : "#/definitions/ActionGroupSignature"
        },
        "ActionGroupExecutor" : {
          "$ref" : "#/definitions/ActionGroupExecutor"
        },
        "ApiSchema" : {
          "$ref" : "#/definitions/APISchema"
        },
        "ActionGroupState" : {
          "$ref" : "#/definitions/ActionGroupState"
        },
        "FunctionSchema" : {
          "$ref" : "#/definitions/FunctionSchema"
        },
        "SkipResourceInUseCheckOnDelete" : {
          "description" : "Specifies whether to allow deleting action group while it is in use.",
          "type" : "boolean",
          "default" : False
        }
      },
      "required" : [ "ActionGroupName" ],
      "additionalProperties" : False
    },
    "AgentCollaboration" : {
      "type" : "string",
      "description" : "Agent collaboration state",
      "enum" : [ "DISABLED", "SUPERVISOR", "SUPERVISOR_ROUTER" ]
    },
    "AgentCollaborator" : {
      "type" : "object",
      "description" : "Agent Collaborator",
      "properties" : {
        "AgentDescriptor" : {
          "type" : "object",
          "description" : "Agent descriptor for agent collaborator",
          "properties" : {
            "AliasArn" : {
              "type" : "string",
              "pattern" : "^arn:aws(|-cn|-us-gov):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent-alias/[0-9a-zA-Z]{10}/[0-9a-zA-Z]{10}$",
              "description" : "Alias ARN for agent descriptor"
            }
          },
          "additionalProperties" : False
        },
        "CollaborationInstruction" : {
          "type" : "string",
          "description" : "Agent collaborator instruction"
        },
        "CollaboratorName" : {
          "type" : "string",
          "description" : "Agent collaborator name"
        },
        "RelayConversationHistory" : {
          "$ref" : "#/definitions/RelayConversationHistory"
        }
      },
      "required" : [ "AgentDescriptor", "CollaborationInstruction", "CollaboratorName" ],
      "additionalProperties" : False
    },
    "AgentKnowledgeBase" : {
      "type" : "object",
      "description" : "Agent Knowledge Base",
      "properties" : {
        "KnowledgeBaseId" : {
          "type" : "string",
          "pattern" : "^[0-9a-zA-Z]{10}$",
          "description" : "Identifier for a resource."
        },
        "Description" : {
          "type" : "string",
          "maxLength" : 200,
          "minLength" : 1,
          "description" : "Description of the Resource."
        },
        "KnowledgeBaseState" : {
          "$ref" : "#/definitions/KnowledgeBaseState"
        }
      },
      "required" : [ "KnowledgeBaseId", "Description" ],
      "additionalProperties" : False
    },
    "AgentStatus" : {
      "type" : "string",
      "description" : "Schema Type for Action APIs.",
      "enum" : [ "CREATING", "PREPARING", "PREPARED", "NOT_PREPARED", "DELETING", "FAILED", "VERSIONING", "UPDATING" ]
    },
    "CreationMode" : {
      "type" : "string",
      "description" : "Creation Mode for Prompt Configuration.",
      "enum" : [ "DEFAULT", "OVERRIDDEN" ]
    },
    "CustomOrchestration" : {
      "type" : "object",
      "description" : "Structure for custom orchestration",
      "properties" : {
        "Executor" : {
          "$ref" : "#/definitions/OrchestrationExecutor"
        }
      },
      "additionalProperties" : False
    },
    "CustomControlMethod" : {
      "type" : "string",
      "description" : "Custom control of action execution",
      "enum" : [ "RETURN_CONTROL" ]
    },
    "FoundationModel" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "pattern" : "^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:(([0-9]{12}:custom-model/[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}(([:][a-z0-9-]{1,63}){0,2})?/[a-z0-9]{12})|(:foundation-model/([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|([0-9]{12}:(inference-profile|application-inference-profile)/[a-zA-Z0-9-:.]+))|(([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([.]?[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}))|(([0-9a-zA-Z][_-]?)+)$",
      "description" : "ARN or name of a Bedrock model."
    },
    "Function" : {
      "type" : "object",
      "description" : "Function definition",
      "properties" : {
        "Name" : {
          "type" : "string",
          "pattern" : "^([0-9a-zA-Z][_-]?){1,100}$",
          "description" : "Name for a resource."
        },
        "Description" : {
          "type" : "string",
          "maxLength" : 1200,
          "minLength" : 1,
          "description" : "Description of function"
        },
        "Parameters" : {
          "$ref" : "#/definitions/ParameterMap"
        },
        "RequireConfirmation" : {
          "$ref" : "#/definitions/RequireConfirmation"
        }
      },
      "required" : [ "Name" ],
      "additionalProperties" : False
    },
    "FunctionSchema" : {
      "description" : "Schema of Functions",
      "type" : "object",
      "title" : "Functions",
      "properties" : {
        "Functions" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Function"
          },
          "description" : "List of Function definitions",
          "insertionOrder" : False
        }
      },
      "required" : [ "Functions" ],
      "additionalProperties" : False
    },
    "GuardrailConfiguration" : {
      "type" : "object",
      "description" : "Configuration for a guardrail.",
      "properties" : {
        "GuardrailIdentifier" : {
          "type" : "string",
          "maxLength" : 2048,
          "pattern" : "^(([a-z0-9]+)|(arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:guardrail/[a-z0-9]+))$",
          "description" : "Identifier for the guardrail, could be the id or the arn"
        },
        "GuardrailVersion" : {
          "type" : "string",
          "pattern" : "^(([0-9]{1,8})|(DRAFT))$",
          "description" : "Version of the guardrail"
        }
      },
      "additionalProperties" : False
    },
    "MemoryConfiguration" : {
      "type" : "object",
      "description" : "Configuration for memory storage",
      "properties" : {
        "EnabledMemoryTypes" : {
          "$ref" : "#/definitions/EnabledMemoryTypes"
        },
        "StorageDays" : {
          "type" : "number",
          "description" : "Maximum number of days to store session details"
        },
        "SessionSummaryConfiguration" : {
          "$ref" : "#/definitions/SessionSummaryConfiguration"
        }
      },
      "additionalProperties" : False
    },
    "EnabledMemoryTypes" : {
      "type" : "array",
      "description" : "Types of session storage persisted in memory",
      "items" : {
        "$ref" : "#/definitions/MemoryType"
      },
      "insertionOrder" : False
    },
    "MemoryType" : {
      "type" : "string",
      "description" : "Memory type",
      "enum" : [ "SESSION_SUMMARY" ]
    },
    "SessionSummaryConfiguration" : {
      "type" : "object",
      "description" : "Configuration for Session Summarization",
      "properties" : {
        "MaxRecentSessions" : {
          "type" : "number",
          "description" : "Maximum number of Sessions to Summarize"
        }
      },
      "additionalProperties" : False
    },
    "InferenceConfiguration" : {
      "type" : "object",
      "description" : "Configuration for inference in prompt configuration",
      "properties" : {
        "Temperature" : {
          "type" : "number",
          "maximum" : 1,
          "minimum" : 0,
          "description" : "Controls randomness, higher values increase diversity"
        },
        "TopP" : {
          "type" : "number",
          "maximum" : 1,
          "minimum" : 0,
          "description" : "Cumulative probability cutoff for token selection"
        },
        "TopK" : {
          "type" : "number",
          "maximum" : 500,
          "minimum" : 0,
          "description" : "Sample from the k most likely next tokens"
        },
        "MaximumLength" : {
          "type" : "number",
          "maximum" : 4096,
          "minimum" : 0,
          "description" : "Maximum length of output"
        },
        "StopSequences" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          },
          "maxItems" : 4,
          "minItems" : 0,
          "description" : "List of stop sequences",
          "insertionOrder" : False
        }
      },
      "additionalProperties" : False
    },
    "KnowledgeBaseState" : {
      "type" : "string",
      "description" : "State of the knowledge base; whether it is enabled or disabled",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "OrchestrationExecutor" : {
      "description" : "Types of executors for custom orchestration strategy",
      "type" : "object",
      "title" : "Lambda",
      "properties" : {
        "Lambda" : {
          "type" : "string",
          "maxLength" : 2048,
          "pattern" : "^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\\d{1}:\\d{12}:function:[a-zA-Z0-9-_\\.]+(:(\\$LATEST|[a-zA-Z0-9-_]+))?$",
          "description" : "ARN of a Lambda."
        }
      },
      "required" : [ "Lambda" ],
      "additionalProperties" : False
    },
    "OrchestrationType" : {
      "type" : "string",
      "description" : "Types of orchestration strategy for agents",
      "enum" : [ "DEFAULT", "CUSTOM_ORCHESTRATION" ]
    },
    "ParameterDetail" : {
      "type" : "object",
      "description" : "Parameter detail",
      "properties" : {
        "Description" : {
          "type" : "string",
          "maxLength" : 500,
          "minLength" : 1,
          "description" : "Description of function parameter."
        },
        "Type" : {
          "$ref" : "#/definitions/Type"
        },
        "Required" : {
          "type" : "boolean",
          "description" : "Information about if a parameter is required for function call. Default to False."
        }
      },
      "required" : [ "Type" ],
      "additionalProperties" : False
    },
    "ParameterMap" : {
      "type" : "object",
      "description" : "A map of parameter name and detail",
      "patternProperties" : {
        "^([0-9a-zA-Z][_-]?){1,100}$" : {
          "$ref" : "#/definitions/ParameterDetail"
        }
      },
      "additionalProperties" : False
    },
    "PromptConfiguration" : {
      "type" : "object",
      "description" : "BasePromptConfiguration per Prompt Type.",
      "properties" : {
        "PromptType" : {
          "$ref" : "#/definitions/PromptType"
        },
        "PromptCreationMode" : {
          "$ref" : "#/definitions/CreationMode"
        },
        "PromptState" : {
          "$ref" : "#/definitions/PromptState"
        },
        "BasePromptTemplate" : {
          "type" : "string",
          "maxLength" : 100000,
          "minLength" : 1,
          "description" : "Base Prompt Template."
        },
        "InferenceConfiguration" : {
          "$ref" : "#/definitions/InferenceConfiguration"
        },
        "ParserMode" : {
          "$ref" : "#/definitions/CreationMode"
        },
        "FoundationModel" : {
          "$ref" : "#/definitions/FoundationModel"
        },
        "AdditionalModelRequestFields" : {
          "$ref" : "#/definitions/AdditionalModelRequestFields"
        }
      },
      "additionalProperties" : False
    },
    "PromptOverrideConfiguration" : {
      "type" : "object",
      "description" : "Configuration for prompt override.",
      "properties" : {
        "PromptConfigurations" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/PromptConfiguration"
          },
          "maxItems" : 10,
          "description" : "List of BasePromptConfiguration",
          "insertionOrder" : False
        },
        "OverrideLambda" : {
          "type" : "string",
          "maxLength" : 2048,
          "pattern" : "^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\\d{1}:\\d{12}:function:[a-zA-Z0-9-_\\.]+(:(\\$LATEST|[a-zA-Z0-9-_]+))?$",
          "description" : "ARN of a Lambda."
        }
      },
      "required" : [ "PromptConfigurations" ],
      "additionalProperties" : False
    },
    "PromptState" : {
      "type" : "string",
      "description" : "Prompt State.",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "PromptType" : {
      "type" : "string",
      "description" : "Prompt Type.",
      "enum" : [ "PRE_PROCESSING", "ORCHESTRATION", "POST_PROCESSING", "ROUTING_CLASSIFIER", "MEMORY_SUMMARIZATION", "KNOWLEDGE_BASE_RESPONSE_GENERATION" ]
    },
    "RelayConversationHistory" : {
      "type" : "string",
      "description" : "Relay conversation history state",
      "enum" : [ "TO_COLLABORATOR", "DISABLED" ]
    },
    "RequireConfirmation" : {
      "type" : "string",
      "description" : "ENUM to check if action requires user confirmation",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "S3Identifier" : {
      "type" : "object",
      "description" : "The identifier for the S3 resource.",
      "properties" : {
        "S3BucketName" : {
          "type" : "string",
          "maxLength" : 63,
          "minLength" : 3,
          "pattern" : "^[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9]$",
          "description" : "A bucket in S3."
        },
        "S3ObjectKey" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 1,
          "pattern" : "^[\\.\\-\\!\\*\\_\\'\\(\\)a-zA-Z0-9][\\.\\-\\!\\*\\_\\'\\(\\)\\/a-zA-Z0-9]*$",
          "description" : "A object key in S3."
        }
      },
      "additionalProperties" : False
    },
    "TagsMap" : {
      "type" : "object",
      "description" : "A map of tag keys and values",
      "patternProperties" : {
        "^[a-zA-Z0-9\\s._:/=+@-]*$" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^[a-zA-Z0-9\\s._:/=+@-]*$",
          "description" : "Value of a tag"
        }
      },
      "additionalProperties" : False
    },
    "Type" : {
      "type" : "string",
      "description" : "Parameter Type",
      "enum" : [ "string", "number", "integer", "boolean", "array" ]
    }
  },
  "properties" : {
    "ActionGroups" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/AgentActionGroup"
      },
      "description" : "List of ActionGroups",
      "insertionOrder" : False
    },
    "AgentArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "pattern" : "^arn:aws(|-cn|-us-gov):bedrock:[a-z0-9-]{1,20}:[0-9]{12}:agent/[0-9a-zA-Z]{10}$",
      "description" : "Arn representation of the Agent."
    },
    "AgentId" : {
      "type" : "string",
      "pattern" : "^[0-9a-zA-Z]{10}$",
      "description" : "Identifier for a resource."
    },
    "AgentName" : {
      "type" : "string",
      "pattern" : "^([0-9a-zA-Z][_-]?){1,100}$",
      "description" : "Name for a resource."
    },
    "AgentResourceRoleArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "description" : "ARN of a IAM role."
    },
    "AgentStatus" : {
      "$ref" : "#/definitions/AgentStatus"
    },
    "AgentVersion" : {
      "type" : "string",
      "maxLength" : 5,
      "minLength" : 5,
      "pattern" : "^DRAFT$",
      "description" : "Draft Agent Version."
    },
    "AutoPrepare" : {
      "description" : "Specifies whether to automatically prepare after creating or updating the agent.",
      "type" : "boolean",
      "default" : False
    },
    "CreatedAt" : {
      "type" : "string",
      "description" : "Time Stamp.",
      "format" : "date-time"
    },
    "CustomOrchestration" : {
      "$ref" : "#/definitions/CustomOrchestration"
    },
    "CustomerEncryptionKeyArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "pattern" : "^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$",
      "description" : "A KMS key ARN"
    },
    "SkipResourceInUseCheckOnDelete" : {
      "description" : "Specifies whether to allow deleting agent while it is in use.",
      "type" : "boolean",
      "default" : False
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 1,
      "description" : "Description of the Resource."
    },
    "FailureReasons" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "description" : "Failure Reason for Error."
      },
      "maxItems" : 2048,
      "description" : "Failure Reasons for Error.",
      "insertionOrder" : False
    },
    "FoundationModel" : {
      "$ref" : "#/definitions/FoundationModel"
    },
    "GuardrailConfiguration" : {
      "$ref" : "#/definitions/GuardrailConfiguration"
    },
    "MemoryConfiguration" : {
      "$ref" : "#/definitions/MemoryConfiguration"
    },
    "IdleSessionTTLInSeconds" : {
      "type" : "number",
      "maximum" : 3600,
      "minimum" : 60,
      "description" : "Max Session Time."
    },
    "AgentCollaboration" : {
      "$ref" : "#/definitions/AgentCollaboration"
    },
    "Instruction" : {
      "type" : "string",
      "minLength" : 40,
      "description" : "Instruction for the agent."
    },
    "KnowledgeBases" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/AgentKnowledgeBase"
      },
      "description" : "List of Agent Knowledge Bases",
      "insertionOrder" : False
    },
    "AgentCollaborators" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/AgentCollaborator"
      },
      "description" : "List of Agent Collaborators",
      "insertionOrder" : False
    },
    "OrchestrationType" : {
      "$ref" : "#/definitions/OrchestrationType"
    },
    "PreparedAt" : {
      "type" : "string",
      "description" : "Time Stamp.",
      "format" : "date-time"
    },
    "PromptOverrideConfiguration" : {
      "$ref" : "#/definitions/PromptOverrideConfiguration"
    },
    "RecommendedActions" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 2048,
        "description" : "The recommended action users can take to resolve an error in failureReasons."
      },
      "maxItems" : 2048,
      "description" : "The recommended actions users can take to resolve an error in failureReasons.",
      "insertionOrder" : False
    },
    "Tags" : {
      "$ref" : "#/definitions/TagsMap"
    },
    "TestAliasTags" : {
      "$ref" : "#/definitions/TagsMap"
    },
    "UpdatedAt" : {
      "type" : "string",
      "description" : "Time Stamp.",
      "format" : "date-time"
    }
  },
  "required" : [ "AgentName" ],
  "readOnlyProperties" : [ "/properties/AgentArn", "/properties/AgentId", "/properties/AgentStatus", "/properties/AgentVersion", "/properties/CreatedAt", "/properties/FailureReasons", "/properties/PreparedAt", "/properties/RecommendedActions", "/properties/UpdatedAt" ],
  "writeOnlyProperties" : [ "/properties/AutoPrepare", "/properties/SkipResourceInUseCheckOnDelete", "/properties/ActionGroups/*/SkipResourceInUseCheckOnDelete" ],
  "primaryIdentifier" : [ "/properties/AgentId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "bedrock:CreateAgent", "bedrock:GetAgent", "bedrock:PrepareAgent", "bedrock:GetAgentKnowledgeBase", "bedrock:AssociateAgentKnowledgeBase", "bedrock:ListAgentKnowledgeBases", "bedrock:CreateAgentActionGroup", "bedrock:GetAgentActionGroup", "bedrock:ListAgentActionGroups", "bedrock:TagResource", "bedrock:ListTagsForResource", "bedrock:CreateGuardrail", "bedrock:CreateGuardrailVersion", "bedrock:GetGuardrail", "bedrock:AssociateAgentCollaborator", "bedrock:GetAgentCollaborator", "bedrock:ListAgentCollaborators", "iam:PassRole", "kms:GenerateDataKeyWithoutPlainText", "kms:ReEncryptFrom", "kms:ReEncryptTo", "kms:Decrypt", "kms:GenerateDataKey" ]
    },
    "read" : {
      "permissions" : [ "bedrock:GetAgent", "bedrock:GetAgentActionGroup", "bedrock:ListAgentActionGroups", "bedrock:GetAgentKnowledgeBase", "bedrock:ListAgentKnowledgeBases", "bedrock:ListTagsForResource", "bedrock:GetGuardrail", "bedrock:GetAgentCollaborator", "bedrock:ListAgentCollaborators", "kms:Decrypt", "kms:GenerateDataKey", "kms:Encrypt" ]
    },
    "update" : {
      "permissions" : [ "bedrock:GetAgent", "bedrock:UpdateAgent", "bedrock:PrepareAgent", "bedrock:GetAgentKnowledgeBase", "bedrock:UpdateAgentKnowledgeBase", "bedrock:AssociateAgentKnowledgeBase", "bedrock:DisassociateAgentKnowledgeBase", "bedrock:ListAgentKnowledgeBases", "bedrock:CreateAgentActionGroup", "bedrock:GetAgentActionGroup", "bedrock:UpdateAgentActionGroup", "bedrock:DeleteAgentActionGroup", "bedrock:ListAgentActionGroups", "bedrock:TagResource", "bedrock:UntagResource", "bedrock:ListTagsForResource", "bedrock:UpdateGuardrail", "bedrock:GetGuardrail", "bedrock:AssociateAgentCollaborator", "bedrock:GetAgentCollaborator", "bedrock:ListAgentCollaborators", "bedrock:DisassociateAgentCollaborator", "bedrock:UpdateAgentCollaborator", "kms:Decrypt", "kms:Encrypt", "kms:GenerateDataKey", "kms:GenerateDataKeyWithoutPlainText", "kms:ReEncryptFrom", "kms:ReEncryptTo", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "bedrock:GetAgent", "bedrock:DeleteAgent", "bedrock:DeleteGuardrail", "bedrock:GetGuardrail", "kms:Decrypt", "kms:Encrypt", "kms:GenerateDataKey" ]
    },
    "list" : {
      "permissions" : [ "bedrock:ListAgents", "bedrock:ListGuardrails" ]
    }
  },
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : True,
    "tagProperty" : "/properties/Tags",
    "tagUpdatable" : True,
    "taggable" : True,
    "permissions" : [ "bedrock:TagResource", "bedrock:UntagResource", "bedrock:ListTagsForResource" ]
  },
  "additionalProperties" : False
}
SCHEMA = {
  "typeName" : "AWS::Wisdom::AIAgent",
  "description" : "Definition of AWS::Wisdom::AIAgent Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "AIAgentAssociationConfigurationType" : {
      "type" : "string",
      "enum" : [ "KNOWLEDGE_BASE" ]
    },
    "AIAgentConfiguration" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "ManualSearchAIAgentConfiguration",
        "properties" : {
          "ManualSearchAIAgentConfiguration" : {
            "$ref" : "#/definitions/ManualSearchAIAgentConfiguration"
          }
        },
        "required" : [ "ManualSearchAIAgentConfiguration" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "AnswerRecommendationAIAgentConfiguration",
        "properties" : {
          "AnswerRecommendationAIAgentConfiguration" : {
            "$ref" : "#/definitions/AnswerRecommendationAIAgentConfiguration"
          }
        },
        "required" : [ "AnswerRecommendationAIAgentConfiguration" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "SelfServiceAIAgentConfiguration",
        "properties" : {
          "SelfServiceAIAgentConfiguration" : {
            "$ref" : "#/definitions/SelfServiceAIAgentConfiguration"
          }
        },
        "required" : [ "SelfServiceAIAgentConfiguration" ],
        "additionalProperties" : False
      } ]
    },
    "AIAgentType" : {
      "type" : "string",
      "enum" : [ "MANUAL_SEARCH", "ANSWER_RECOMMENDATION", "SELF_SERVICE" ]
    },
    "SelfServiceAIAgentConfiguration" : {
      "type" : "object",
      "properties" : {
        "SelfServicePreProcessingAIPromptId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "SelfServiceAnswerGenerationAIPromptId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "SelfServiceAIGuardrailId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "AssociationConfigurations" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AssociationConfiguration"
          }
        }
      },
      "additionalProperties" : False
    },
    "AnswerRecommendationAIAgentConfiguration" : {
      "type" : "object",
      "properties" : {
        "IntentLabelingGenerationAIPromptId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "QueryReformulationAIPromptId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "AnswerGenerationAIPromptId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "AnswerGenerationAIGuardrailId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "AssociationConfigurations" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AssociationConfiguration"
          }
        },
        "Locale" : {
          "type" : "string",
          "minLength" : 1
        }
      },
      "additionalProperties" : False
    },
    "AssociationConfiguration" : {
      "type" : "object",
      "properties" : {
        "AssociationId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
        },
        "AssociationType" : {
          "$ref" : "#/definitions/AIAgentAssociationConfigurationType"
        },
        "AssociationConfigurationData" : {
          "$ref" : "#/definitions/AssociationConfigurationData"
        }
      },
      "additionalProperties" : False
    },
    "AssociationConfigurationData" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "KnowledgeBaseAssociationConfigurationData",
        "properties" : {
          "KnowledgeBaseAssociationConfigurationData" : {
            "$ref" : "#/definitions/KnowledgeBaseAssociationConfigurationData"
          }
        },
        "required" : [ "KnowledgeBaseAssociationConfigurationData" ],
        "additionalProperties" : False
      } ]
    },
    "KnowledgeBaseAssociationConfigurationData" : {
      "type" : "object",
      "properties" : {
        "ContentTagFilter" : {
          "$ref" : "#/definitions/TagFilter"
        },
        "MaxResults" : {
          "type" : "number",
          "maximum" : 100,
          "minimum" : 1
        },
        "OverrideKnowledgeBaseSearchType" : {
          "$ref" : "#/definitions/KnowledgeBaseSearchType"
        }
      },
      "additionalProperties" : False
    },
    "KnowledgeBaseSearchType" : {
      "type" : "string",
      "enum" : [ "HYBRID", "SEMANTIC" ]
    },
    "ManualSearchAIAgentConfiguration" : {
      "type" : "object",
      "properties" : {
        "AnswerGenerationAIPromptId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "AnswerGenerationAIGuardrailId" : {
          "type" : "string",
          "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$"
        },
        "AssociationConfigurations" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/AssociationConfiguration"
          }
        },
        "Locale" : {
          "type" : "string",
          "minLength" : 1
        }
      },
      "additionalProperties" : False
    },
    "OrCondition" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "AndConditions",
        "properties" : {
          "AndConditions" : {
            "type" : "array",
            "items" : {
              "$ref" : "#/definitions/TagCondition"
            }
          }
        },
        "required" : [ "AndConditions" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "TagCondition",
        "properties" : {
          "TagCondition" : {
            "$ref" : "#/definitions/TagCondition"
          }
        },
        "required" : [ "TagCondition" ],
        "additionalProperties" : False
      } ]
    },
    "TagCondition" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "required" : [ "Key" ],
      "additionalProperties" : False
    },
    "TagFilter" : {
      "oneOf" : [ {
        "type" : "object",
        "title" : "TagCondition",
        "properties" : {
          "TagCondition" : {
            "$ref" : "#/definitions/TagCondition"
          }
        },
        "required" : [ "TagCondition" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "AndConditions",
        "properties" : {
          "AndConditions" : {
            "type" : "array",
            "items" : {
              "$ref" : "#/definitions/TagCondition"
            }
          }
        },
        "required" : [ "AndConditions" ],
        "additionalProperties" : False
      }, {
        "type" : "object",
        "title" : "OrConditions",
        "properties" : {
          "OrConditions" : {
            "type" : "array",
            "items" : {
              "$ref" : "#/definitions/OrCondition"
            }
          }
        },
        "required" : [ "OrConditions" ],
        "additionalProperties" : False
      } ]
    },
    "Tags" : {
      "type" : "object",
      "patternProperties" : {
        "^(?!aws:)[a-zA-Z+-=._:/]+$" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AIAgentId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}$"
    },
    "AIAgentArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$"
    },
    "AssistantId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$"
    },
    "AssistantArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$"
    },
    "Configuration" : {
      "$ref" : "#/definitions/AIAgentConfiguration"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9\\s_.,-]+"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9\\s_.,-]+"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    },
    "Type" : {
      "$ref" : "#/definitions/AIAgentType"
    },
    "ModifiedTimeSeconds" : {
      "type" : "number"
    }
  },
  "required" : [ "AssistantId", "Configuration", "Type" ],
  "readOnlyProperties" : [ "/properties/AIAgentArn", "/properties/AIAgentId", "/properties/AssistantArn", "/properties/ModifiedTimeSeconds" ],
  "createOnlyProperties" : [ "/properties/AssistantId", "/properties/Name", "/properties/Tags", "/properties/Type" ],
  "primaryIdentifier" : [ "/properties/AIAgentId", "/properties/AssistantId" ],
  "additionalIdentifiers" : [ [ "/properties/AIAgentArn", "/properties/AssistantArn" ] ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "wisdom:TagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "wisdom:CreateAIAgent", "wisdom:TagResource" ]
    },
    "read" : {
      "permissions" : [ "wisdom:GetAIAgent" ]
    },
    "update" : {
      "permissions" : [ "wisdom:UpdateAIAgent" ]
    },
    "delete" : {
      "permissions" : [ "wisdom:DeleteAIAgent" ]
    },
    "list" : {
      "permissions" : [ "wisdom:ListAIAgents" ],
      "handlerSchema" : {
        "properties" : {
          "AssistantId" : {
            "$ref" : "resource-schema.json#/properties/AssistantId"
          }
        },
        "required" : [ "AssistantId" ]
      }
    }
  },
  "additionalProperties" : False
}
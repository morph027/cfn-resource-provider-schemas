SCHEMA = {
  "typeName" : "AWS::Wisdom::AIGuardrail",
  "description" : "Definition of AWS::Wisdom::AIGuardrail Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "AIGuardrailContentPolicyConfig" : {
      "type" : "object",
      "description" : "Content policy config for a guardrail.",
      "properties" : {
        "FiltersConfig" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GuardrailContentFilterConfig"
          },
          "maxItems" : 6,
          "minItems" : 1,
          "description" : "List of content filter configs in content policy."
        }
      },
      "required" : [ "FiltersConfig" ],
      "additionalProperties" : False
    },
    "AIGuardrailContextualGroundingPolicyConfig" : {
      "type" : "object",
      "description" : "Contextual grounding policy config for a guardrail.",
      "properties" : {
        "FiltersConfig" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GuardrailContextualGroundingFilterConfig"
          },
          "minItems" : 1,
          "description" : "List of contextual grounding filter configs."
        }
      },
      "required" : [ "FiltersConfig" ],
      "additionalProperties" : False
    },
    "AIGuardrailSensitiveInformationPolicyConfig" : {
      "type" : "object",
      "description" : "Sensitive information policy config for a guardrail.",
      "properties" : {
        "PiiEntitiesConfig" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GuardrailPiiEntityConfig"
          },
          "minItems" : 1,
          "uniqueItems" : True,
          "description" : "List of entities."
        },
        "RegexesConfig" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GuardrailRegexConfig"
          },
          "minItems" : 1,
          "description" : "List of regex."
        }
      },
      "additionalProperties" : False
    },
    "AIGuardrailTopicPolicyConfig" : {
      "type" : "object",
      "description" : "Topic policy config for a guardrail.",
      "properties" : {
        "TopicsConfig" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GuardrailTopicConfig"
          },
          "minItems" : 1,
          "description" : "List of topic configs in topic policy."
        }
      },
      "required" : [ "TopicsConfig" ],
      "additionalProperties" : False
    },
    "AIGuardrailWordPolicyConfig" : {
      "type" : "object",
      "description" : "Word policy config for a guardrail.",
      "properties" : {
        "WordsConfig" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GuardrailWordConfig"
          },
          "minItems" : 1,
          "description" : "List of custom word configs."
        },
        "ManagedWordListsConfig" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/GuardrailManagedWordsConfig"
          },
          "description" : "A config for the list of managed words."
        }
      },
      "additionalProperties" : False
    },
    "GuardrailContentFilterConfig" : {
      "type" : "object",
      "description" : "Content filter config in content policy.",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/GuardrailContentFilterType"
        },
        "InputStrength" : {
          "$ref" : "#/definitions/GuardrailFilterStrength"
        },
        "OutputStrength" : {
          "$ref" : "#/definitions/GuardrailFilterStrength"
        }
      },
      "required" : [ "InputStrength", "OutputStrength", "Type" ],
      "additionalProperties" : False
    },
    "GuardrailContentFilterType" : {
      "type" : "string",
      "description" : "Type of text to text filter in content policy",
      "enum" : [ "SEXUAL", "VIOLENCE", "HATE", "INSULTS", "MISCONDUCT", "PROMPT_ATTACK" ]
    },
    "GuardrailContextualGroundingFilterConfig" : {
      "type" : "object",
      "description" : "A config for grounding filter.",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/GuardrailContextualGroundingFilterType"
        },
        "Threshold" : {
          "type" : "number",
          "default" : 0,
          "minimum" : 0,
          "description" : "The threshold for this filter."
        }
      },
      "required" : [ "Threshold", "Type" ],
      "additionalProperties" : False
    },
    "GuardrailContextualGroundingFilterType" : {
      "type" : "string",
      "description" : "Type of contextual grounding filter",
      "enum" : [ "GROUNDING", "RELEVANCE" ]
    },
    "GuardrailFilterStrength" : {
      "type" : "string",
      "description" : "Strength for filters",
      "enum" : [ "NONE", "LOW", "MEDIUM", "HIGH" ]
    },
    "GuardrailManagedWordsConfig" : {
      "type" : "object",
      "description" : "A managed words config.",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/GuardrailManagedWordsType"
        }
      },
      "required" : [ "Type" ],
      "additionalProperties" : False
    },
    "GuardrailManagedWordsType" : {
      "type" : "string",
      "description" : "Options for managed words.",
      "enum" : [ "PROFANITY" ]
    },
    "GuardrailPiiEntityConfig" : {
      "type" : "object",
      "description" : "Pii entity configuration.",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/GuardrailPiiEntityType"
        },
        "Action" : {
          "$ref" : "#/definitions/GuardrailSensitiveInformationAction"
        }
      },
      "required" : [ "Action", "Type" ],
      "additionalProperties" : False
    },
    "GuardrailPiiEntityType" : {
      "type" : "string",
      "description" : "The currently supported PII entities",
      "enum" : [ "ADDRESS", "AGE", "AWS_ACCESS_KEY", "AWS_SECRET_KEY", "CA_HEALTH_NUMBER", "CA_SOCIAL_INSURANCE_NUMBER", "CREDIT_DEBIT_CARD_CVV", "CREDIT_DEBIT_CARD_EXPIRY", "CREDIT_DEBIT_CARD_NUMBER", "DRIVER_ID", "EMAIL", "INTERNATIONAL_BANK_ACCOUNT_NUMBER", "IP_ADDRESS", "LICENSE_PLATE", "MAC_ADDRESS", "NAME", "PASSWORD", "PHONE", "PIN", "SWIFT_CODE", "UK_NATIONAL_HEALTH_SERVICE_NUMBER", "UK_NATIONAL_INSURANCE_NUMBER", "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER", "URL", "USERNAME", "US_BANK_ACCOUNT_NUMBER", "US_BANK_ROUTING_NUMBER", "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER", "US_PASSPORT_NUMBER", "US_SOCIAL_SECURITY_NUMBER", "VEHICLE_IDENTIFICATION_NUMBER" ]
    },
    "GuardrailRegexConfig" : {
      "type" : "object",
      "description" : "A regex configuration.",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 1,
          "description" : "The regex name."
        },
        "Description" : {
          "type" : "string",
          "maxLength" : 1000,
          "minLength" : 1,
          "description" : "The regex description."
        },
        "Pattern" : {
          "type" : "string",
          "minLength" : 1,
          "description" : "The regex pattern."
        },
        "Action" : {
          "$ref" : "#/definitions/GuardrailSensitiveInformationAction"
        }
      },
      "required" : [ "Action", "Name", "Pattern" ],
      "additionalProperties" : False
    },
    "GuardrailSensitiveInformationAction" : {
      "type" : "string",
      "description" : "Options for sensitive information action.",
      "enum" : [ "BLOCK", "ANONYMIZE" ]
    },
    "GuardrailTopicConfig" : {
      "type" : "object",
      "description" : "Topic config in topic policy.",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 1,
          "pattern" : "^[0-9a-zA-Z-_ !?.]+$",
          "description" : "Name of topic in topic policy"
        },
        "Definition" : {
          "type" : "string",
          "maxLength" : 200,
          "minLength" : 1,
          "description" : "Definition of topic in topic policy"
        },
        "Examples" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 100,
            "minLength" : 1,
            "description" : "Text example in topic policy"
          },
          "minItems" : 0,
          "description" : "List of text examples"
        },
        "Type" : {
          "$ref" : "#/definitions/GuardrailTopicType"
        }
      },
      "required" : [ "Definition", "Name", "Type" ],
      "additionalProperties" : False
    },
    "GuardrailTopicType" : {
      "type" : "string",
      "description" : "Type of topic in a policy",
      "enum" : [ "DENY" ]
    },
    "GuardrailWordConfig" : {
      "type" : "object",
      "description" : "A custom word config.",
      "properties" : {
        "Text" : {
          "type" : "string",
          "minLength" : 1,
          "description" : "The custom word text."
        }
      },
      "required" : [ "Text" ],
      "additionalProperties" : False
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
    "AssistantId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$"
    },
    "AssistantArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$"
    },
    "AIGuardrailArn" : {
      "type" : "string",
      "pattern" : "^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}$"
    },
    "AIGuardrailId" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}$"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 255,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9\\s_.,-]+"
    },
    "BlockedInputMessaging" : {
      "type" : "string",
      "maxLength" : 500,
      "minLength" : 1,
      "description" : "Messaging for when violations are detected in text"
    },
    "BlockedOutputsMessaging" : {
      "type" : "string",
      "maxLength" : 500,
      "minLength" : 1,
      "description" : "Messaging for when violations are detected in text"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 1,
      "description" : "Description of the guardrail or its version"
    },
    "TopicPolicyConfig" : {
      "$ref" : "#/definitions/AIGuardrailTopicPolicyConfig"
    },
    "ContentPolicyConfig" : {
      "$ref" : "#/definitions/AIGuardrailContentPolicyConfig"
    },
    "WordPolicyConfig" : {
      "$ref" : "#/definitions/AIGuardrailWordPolicyConfig"
    },
    "SensitiveInformationPolicyConfig" : {
      "$ref" : "#/definitions/AIGuardrailSensitiveInformationPolicyConfig"
    },
    "ContextualGroundingPolicyConfig" : {
      "$ref" : "#/definitions/AIGuardrailContextualGroundingPolicyConfig"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "required" : [ "AssistantId", "BlockedInputMessaging", "BlockedOutputsMessaging" ],
  "readOnlyProperties" : [ "/properties/AIGuardrailArn", "/properties/AIGuardrailId", "/properties/AssistantArn" ],
  "createOnlyProperties" : [ "/properties/AssistantId", "/properties/Name", "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/AIGuardrailId", "/properties/AssistantId" ],
  "additionalIdentifiers" : [ [ "/properties/AIGuardrailArn", "/properties/AssistantArn" ] ],
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
      "permissions" : [ "wisdom:CreateAIGuardrail", "wisdom:TagResource" ]
    },
    "read" : {
      "permissions" : [ "wisdom:GetAIGuardrail" ]
    },
    "update" : {
      "permissions" : [ "wisdom:UpdateAIGuardrail" ]
    },
    "delete" : {
      "permissions" : [ "wisdom:DeleteAIGuardrail" ]
    },
    "list" : {
      "permissions" : [ "wisdom:ListAIGuardrails" ],
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
SCHEMA = {
  "typeName" : "AWS::SecurityHub::ConfigurationPolicy",
  "description" : "The AWS::SecurityHub::ConfigurationPolicy resource represents the Central Configuration Policy in your account.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securityhub",
  "definitions" : {
    "Tags" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "patternProperties" : {
        "^(?!aws:)[a-zA-Z+-=._:/]{1,128}$" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      }
    },
    "ParameterValue" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "An object that includes the data type of a security control parameter and its current value.",
      "maxProperties" : 1,
      "minProperties" : 1,
      "properties" : {
        "Boolean" : {
          "type" : "boolean",
          "description" : "A control parameter that is a boolean."
        },
        "Double" : {
          "type" : "number",
          "description" : "A control parameter that is a double."
        },
        "Enum" : {
          "type" : "string",
          "description" : "A control parameter that is an enum.",
          "maxLength" : 2048
        },
        "EnumList" : {
          "type" : "array",
          "description" : "A control parameter that is a list of enums.",
          "maxItems" : 100,
          "insertionOrder" : True,
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "Integer" : {
          "type" : "integer",
          "description" : "A control parameter that is an integer."
        },
        "IntegerList" : {
          "type" : "array",
          "description" : "A control parameter that is a list of integers.",
          "maxItems" : 100,
          "insertionOrder" : True,
          "uniqueItems" : True,
          "items" : {
            "type" : "integer"
          }
        },
        "String" : {
          "type" : "string",
          "description" : "A control parameter that is a string.",
          "maxLength" : 2048
        },
        "StringList" : {
          "type" : "array",
          "description" : "A control parameter that is a list of strings.",
          "maxItems" : 100,
          "insertionOrder" : True,
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "maxLength" : 2048
          }
        }
      }
    },
    "ParameterConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "An object that provides the current value of a security control parameter and identifies whether it has been customized.",
      "properties" : {
        "ValueType" : {
          "type" : "string",
          "description" : "Identifies whether a control parameter uses a custom user-defined value or subscribes to the default AWS Security Hub behavior.",
          "enum" : [ "DEFAULT", "CUSTOM" ]
        },
        "Value" : {
          "$ref" : "#/definitions/ParameterValue"
        }
      },
      "required" : [ "ValueType" ]
    },
    "SecurityControlCustomParameter" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "An object of security control and control parameter value that are included in a configuration policy.",
      "properties" : {
        "Parameters" : {
          "type" : "object",
          "minProperties" : 1,
          "description" : "An object that specifies parameter values for a control in a configuration policy.",
          "additionalProperties" : False,
          "patternProperties" : {
            "^[-_+=.:/@\\w\\s]{1,128}$" : {
              "$ref" : "#/definitions/ParameterConfiguration"
            }
          }
        },
        "SecurityControlId" : {
          "type" : "string",
          "description" : "The ID of the security control.",
          "maxLength" : 2048
        }
      }
    },
    "SecurityControlsConfiguration" : {
      "type" : "object",
      "description" : "An object that defines which security controls are enabled in an AWS Security Hub configuration policy.",
      "additionalProperties" : False,
      "properties" : {
        "DisabledSecurityControlIdentifiers" : {
          "type" : "array",
          "description" : "A list of security controls that are disabled in the configuration policy",
          "maxItems" : 1000,
          "insertionOrder" : True,
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "EnabledSecurityControlIdentifiers" : {
          "type" : "array",
          "description" : "A list of security controls that are enabled in the configuration policy.",
          "maxItems" : 1000,
          "insertionOrder" : True,
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "SecurityControlCustomParameters" : {
          "type" : "array",
          "description" : "A list of security controls and control parameter values that are included in a configuration policy.",
          "maxItems" : 1000,
          "insertionOrder" : True,
          "uniqueItems" : True,
          "items" : {
            "$ref" : "#/definitions/SecurityControlCustomParameter"
          }
        }
      }
    },
    "SecurityHubPolicy" : {
      "type" : "object",
      "description" : "An object that defines how AWS Security Hub is configured.",
      "additionalProperties" : False,
      "properties" : {
        "EnabledStandardIdentifiers" : {
          "type" : "array",
          "description" : "A list that defines which security standards are enabled in the configuration policy.",
          "maxItems" : 1000,
          "insertionOrder" : True,
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "maxLength" : 2048
          }
        },
        "ServiceEnabled" : {
          "description" : "Indicates whether Security Hub is enabled in the policy.",
          "type" : "boolean"
        },
        "SecurityControlsConfiguration" : {
          "$ref" : "#/definitions/SecurityControlsConfiguration"
        }
      }
    },
    "Policy" : {
      "description" : "An object that defines how Security Hub is configured.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SecurityHub" : {
          "$ref" : "#/definitions/SecurityHubPolicy"
        }
      }
    }
  },
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the configuration policy.",
      "type" : "string",
      "pattern" : "^arn:aws\\S*:securityhub:[a-z0-9-]+:[0-9]{12}:configuration-policy/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    },
    "Name" : {
      "description" : "The name of the configuration policy.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Description" : {
      "description" : "The description of the configuration policy.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 512
    },
    "ConfigurationPolicy" : {
      "$ref" : "#/definitions/Policy"
    },
    "Id" : {
      "description" : "The universally unique identifier (UUID) of the configuration policy.",
      "type" : "string",
      "pattern" : "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    },
    "CreatedAt" : {
      "description" : "The date and time, in UTC and ISO 8601 format.",
      "type" : "string"
    },
    "UpdatedAt" : {
      "description" : "The date and time, in UTC and ISO 8601 format.",
      "type" : "string"
    },
    "ServiceEnabled" : {
      "type" : "boolean",
      "description" : "Indicates whether the service that the configuration policy applies to is enabled in the policy."
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "additionalProperties" : False,
  "required" : [ "ConfigurationPolicy", "Name" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/CreatedAt", "/properties/UpdatedAt", "/properties/ServiceEnabled" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "securityhub:ListTagsForResource", "securityhub:TagResource", "securityhub:UntagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "securityhub:CreateConfigurationPolicy", "securityhub:TagResource", "securityhub:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "securityhub:GetConfigurationPolicy", "securityhub:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "securityhub:UpdateConfigurationPolicy", "securityhub:TagResource", "securityhub:UntagResource", "securityhub:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "securityhub:GetConfigurationPolicy", "securityhub:DeleteConfigurationPolicy" ]
    },
    "list" : {
      "permissions" : [ "securityhub:ListConfigurationPolicies", "securityhub:ListTagsForResource" ]
    }
  }
}
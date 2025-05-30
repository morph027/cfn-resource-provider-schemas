SCHEMA = {
  "typeName" : "AWS::Config::OrganizationConfigRule",
  "description" : "Resource Type definition for AWS::Config::OrganizationConfigRule",
  "additionalProperties" : False,
  "properties" : {
    "OrganizationCustomRuleMetadata" : {
      "$ref" : "#/definitions/OrganizationCustomRuleMetadata"
    },
    "OrganizationManagedRuleMetadata" : {
      "$ref" : "#/definitions/OrganizationManagedRuleMetadata"
    },
    "ExcludedAccounts" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "OrganizationConfigRuleName" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "OrganizationCustomPolicyRuleMetadata" : {
      "$ref" : "#/definitions/OrganizationCustomPolicyRuleMetadata"
    }
  },
  "definitions" : {
    "OrganizationManagedRuleMetadata" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TagKeyScope" : {
          "type" : "string"
        },
        "TagValueScope" : {
          "type" : "string"
        },
        "Description" : {
          "type" : "string"
        },
        "ResourceIdScope" : {
          "type" : "string"
        },
        "RuleIdentifier" : {
          "type" : "string"
        },
        "ResourceTypesScope" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "MaximumExecutionFrequency" : {
          "type" : "string"
        },
        "InputParameters" : {
          "type" : "string"
        }
      },
      "required" : [ "RuleIdentifier" ]
    },
    "OrganizationCustomRuleMetadata" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TagKeyScope" : {
          "type" : "string"
        },
        "TagValueScope" : {
          "type" : "string"
        },
        "Description" : {
          "type" : "string"
        },
        "ResourceIdScope" : {
          "type" : "string"
        },
        "LambdaFunctionArn" : {
          "type" : "string"
        },
        "OrganizationConfigRuleTriggerTypes" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "ResourceTypesScope" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "MaximumExecutionFrequency" : {
          "type" : "string"
        },
        "InputParameters" : {
          "type" : "string"
        }
      },
      "required" : [ "LambdaFunctionArn", "OrganizationConfigRuleTriggerTypes" ]
    },
    "OrganizationCustomPolicyRuleMetadata" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "TagKeyScope" : {
          "type" : "string"
        },
        "TagValueScope" : {
          "type" : "string"
        },
        "Runtime" : {
          "type" : "string"
        },
        "PolicyText" : {
          "type" : "string"
        },
        "Description" : {
          "type" : "string"
        },
        "ResourceIdScope" : {
          "type" : "string"
        },
        "OrganizationConfigRuleTriggerTypes" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "DebugLogDeliveryAccounts" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "ResourceTypesScope" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "MaximumExecutionFrequency" : {
          "type" : "string"
        },
        "InputParameters" : {
          "type" : "string"
        }
      },
      "required" : [ "Runtime", "PolicyText" ]
    }
  },
  "required" : [ "OrganizationConfigRuleName" ],
  "createOnlyProperties" : [ "/properties/OrganizationConfigRuleName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}
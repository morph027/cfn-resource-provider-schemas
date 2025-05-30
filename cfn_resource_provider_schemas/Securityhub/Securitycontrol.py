SCHEMA = {
  "typeName" : "AWS::SecurityHub::SecurityControl",
  "description" : "A security control in Security Hub describes a security best practice related to a specific resource.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securityhub",
  "definitions" : {
    "NonEmptyString" : {
      "type" : "string",
      "pattern" : ".*\\S.*"
    },
    "NonEmptyStringList" : {
      "items" : {
        "$ref" : "#/definitions/NonEmptyString"
      },
      "type" : "array"
    },
    "IntegerList" : {
      "items" : {
        "type" : "integer"
      },
      "type" : "array"
    },
    "Parameters" : {
      "type" : "object",
      "patternProperties" : {
        ".*\\S.*" : {
          "$ref" : "#/definitions/ParameterConfiguration"
        }
      },
      "additionalProperties" : False
    },
    "ParameterConfiguration" : {
      "type" : "object",
      "properties" : {
        "ValueType" : {
          "type" : "string",
          "enum" : [ "DEFAULT", "CUSTOM" ]
        },
        "Value" : {
          "$ref" : "#/definitions/ParameterValue"
        }
      },
      "additionalProperties" : False,
      "required" : [ "ValueType" ]
    },
    "ParameterValue" : {
      "type" : "object",
      "properties" : {
        "Boolean" : {
          "description" : "A control parameter that is a boolean.",
          "type" : "boolean"
        },
        "Double" : {
          "description" : "A control parameter that is a double.",
          "type" : "number"
        },
        "Enum" : {
          "description" : "A control parameter that is a enum.",
          "$ref" : "#/definitions/NonEmptyString"
        },
        "EnumList" : {
          "description" : "A control parameter that is a list of enums.",
          "$ref" : "#/definitions/NonEmptyStringList"
        },
        "Integer" : {
          "description" : "A control parameter that is a integer.",
          "type" : "integer"
        },
        "IntegerList" : {
          "description" : "A control parameter that is a list of integers.",
          "$ref" : "#/definitions/IntegerList"
        },
        "String" : {
          "description" : "A control parameter that is a string.",
          "$ref" : "#/definitions/NonEmptyString"
        },
        "StringList" : {
          "description" : "A control parameter that is a list of strings.",
          "$ref" : "#/definitions/NonEmptyStringList"
        }
      },
      "oneOf" : [ {
        "required" : [ "Boolean" ]
      }, {
        "required" : [ "Double" ]
      }, {
        "required" : [ "Enum" ]
      }, {
        "required" : [ "EnumList" ]
      }, {
        "required" : [ "Integer" ]
      }, {
        "required" : [ "IntegerList" ]
      }, {
        "required" : [ "String" ]
      }, {
        "required" : [ "StringList" ]
      } ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "SecurityControlId" : {
      "description" : "The unique identifier of a security control across standards. Values for this field typically consist of an AWS service name and a number, such as APIGateway.3.",
      "$ref" : "#/definitions/NonEmptyString"
    },
    "SecurityControlArn" : {
      "description" : "The Amazon Resource Name (ARN) for a security control across standards, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1`. This parameter doesn't mention a specific standard.",
      "$ref" : "#/definitions/NonEmptyString"
    },
    "LastUpdateReason" : {
      "description" : "The most recent reason for updating the customizable properties of a security control. This differs from the UpdateReason field of the BatchUpdateStandardsControlAssociations API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.",
      "type" : "string",
      "pattern" : "^([^\u0000-]|[-_ a-zA-Z0-9])+$"
    },
    "Parameters" : {
      "description" : "An object that identifies the name of a control parameter, its current value, and whether it has been customized.",
      "$ref" : "#/definitions/Parameters"
    }
  },
  "additionalProperties" : False,
  "anyOf" : [ {
    "required" : [ "SecurityControlId" ]
  }, {
    "required" : [ "SecurityControlArn" ]
  } ],
  "required" : [ "Parameters" ],
  "createOnlyProperties" : [ "/properties/SecurityControlId" ],
  "primaryIdentifier" : [ "/properties/SecurityControlId" ],
  "additionalIdentifiers" : [ [ "/properties/SecurityControlArn" ] ],
  "tagging" : {
    "taggable" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "securityhub:BatchGetSecurityControls", "securityhub:DescribeStandardsControls", "securityhub:UpdateSecurityControl", "securityhub:UpdateStandardsControl" ],
      "timeoutInMinutes" : 2160
    },
    "read" : {
      "permissions" : [ "securityhub:BatchGetSecurityControls", "securityhub:DescribeStandardsControls" ]
    },
    "update" : {
      "permissions" : [ "securityhub:BatchGetSecurityControls", "securityhub:DescribeStandardsControls", "securityhub:UpdateSecurityControl", "securityhub:UpdateStandardsControl" ],
      "timeoutInMinutes" : 2160
    },
    "delete" : {
      "permissions" : [ "securityhub:BatchGetSecurityControls", "securityhub:DescribeStandardsControls", "securityhub:UpdateSecurityControl", "securityhub:UpdateStandardsControl" ],
      "timeoutInMinutes" : 2160
    },
    "list" : {
      "permissions" : [ "securityhub:BatchGetSecurityControls", "securityhub:DescribeStandardsControls", "securityhub:ListSecurityControlDefinitions" ]
    }
  }
}
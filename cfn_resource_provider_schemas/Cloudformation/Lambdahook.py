SCHEMA = {
  "typeName" : "AWS::CloudFormation::LambdaHook",
  "description" : "This is a CloudFormation resource for the first-party AWS::Hooks::LambdaHook.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Role" : {
      "description" : "IAM Role ARN",
      "pattern" : "arn:.+:iam::[0-9]{12}:role/.+",
      "type" : "string",
      "maxLength" : 256
    },
    "StackRole" : {
      "description" : "IAM Stack Role ARN filter",
      "type" : "string",
      "maxLength" : 256,
      "anyOf" : [ {
        "pattern" : "arn:.+:iam::[0-9]{12}:role/.+"
      }, {
        "pattern" : "^(arn:.+:iam::((?!\\*|\\?)[0-9]{12}|(?=.*\\*)[0-9*?]{1,12}|[0-9?]{12}):role/.+|\\*)$"
      } ]
    },
    "StackName" : {
      "pattern" : "^[a-zA-Z*?][-a-zA-Z0-9*?]*$",
      "description" : "CloudFormation Stack name",
      "type" : "string",
      "maxLength" : 128
    },
    "TargetOperation" : {
      "description" : "Which operations should this Hook run against? Resource changes, stacks or change sets.",
      "type" : "string",
      "enum" : [ "RESOURCE", "STACK", "CHANGE_SET", "CLOUD_CONTROL" ]
    },
    "TargetName" : {
      "description" : "Type name of hook target. Hook targets are the destination where hooks will be invoked against.",
      "type" : "string",
      "pattern" : "^(?!.*\\*\\?).*$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "Action" : {
      "description" : "Target actions are the type of operation hooks will be executed at.",
      "type" : "string",
      "enum" : [ "CREATE", "UPDATE", "DELETE" ]
    },
    "InvocationPoint" : {
      "description" : "Invocation points are the point in provisioning workflow where hooks will be executed.",
      "type" : "string",
      "enum" : [ "PRE_PROVISION" ]
    },
    "HookTarget" : {
      "description" : "Hook targets are the destination where hooks will be invoked against.",
      "type" : "object",
      "properties" : {
        "TargetName" : {
          "$ref" : "#/definitions/TargetName"
        },
        "Action" : {
          "$ref" : "#/definitions/Action"
        },
        "InvocationPoint" : {
          "$ref" : "#/definitions/InvocationPoint"
        }
      },
      "additionalProperties" : False,
      "required" : [ "TargetName", "Action", "InvocationPoint" ]
    }
  },
  "properties" : {
    "LambdaFunction" : {
      "description" : "Amazon Resource Name (ARN), Partial ARN, name, version, or alias of the Lambda function to invoke with this hook.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 170,
      "pattern" : "(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}(-gov)?(-iso([a-z])?)?-[a-z]+-\\d{1}:)?(\\d{12}:)?(function:)?([a-zA-Z0-9-_]+)(:(\\$LATEST|[a-zA-Z0-9-_]+))?"
    },
    "HookStatus" : {
      "default" : "ENABLED",
      "description" : "Attribute to specify which stacks this hook applies to or should get invoked for",
      "type" : "string",
      "enum" : [ "ENABLED", "DISABLED" ]
    },
    "TargetOperations" : {
      "description" : "Which operations should this Hook run against? Resource changes, stacks or change sets.",
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/TargetOperation"
      }
    },
    "FailureMode" : {
      "description" : "Attribute to specify CloudFormation behavior on hook failure.",
      "type" : "string",
      "enum" : [ "FAIL", "WARN" ]
    },
    "TargetFilters" : {
      "description" : "Attribute to specify which targets should invoke the hook",
      "type" : "object",
      "oneOf" : [ {
        "type" : "object",
        "minProperties" : 1,
        "properties" : {
          "TargetNames" : {
            "description" : "List of type names that the hook is going to target",
            "type" : "array",
            "minItems" : 1,
            "maxItems" : 50,
            "uniqueItems" : True,
            "insertionOrder" : False,
            "items" : {
              "$ref" : "#/definitions/TargetName"
            }
          },
          "Actions" : {
            "description" : "List of actions that the hook is going to target",
            "type" : "array",
            "minItems" : 1,
            "maxItems" : 50,
            "uniqueItems" : True,
            "insertionOrder" : False,
            "items" : {
              "$ref" : "#/definitions/Action"
            }
          },
          "InvocationPoints" : {
            "description" : "List of invocation points that the hook is going to target",
            "type" : "array",
            "minItems" : 1,
            "maxItems" : 50,
            "uniqueItems" : True,
            "insertionOrder" : False,
            "items" : {
              "$ref" : "#/definitions/InvocationPoint"
            }
          }
        },
        "additionalProperties" : False
      }, {
        "type" : "object",
        "properties" : {
          "Targets" : {
            "description" : "List of hook targets",
            "type" : "array",
            "minItems" : 1,
            "maxItems" : 50,
            "uniqueItems" : True,
            "items" : {
              "$ref" : "#/definitions/HookTarget"
            }
          }
        },
        "additionalProperties" : False,
        "required" : [ "Targets" ]
      } ]
    },
    "StackFilters" : {
      "description" : "Filters to allow hooks to target specific stack attributes",
      "type" : "object",
      "properties" : {
        "FilteringCriteria" : {
          "description" : "Attribute to specify the filtering behavior. ANY will make the Hook pass if one filter matches. ALL will make the Hook pass if all filters match",
          "type" : "string",
          "default" : "ALL",
          "enum" : [ "ALL", "ANY" ]
        },
        "StackNames" : {
          "description" : "List of stack names as filters",
          "type" : "object",
          "additionalProperties" : False,
          "minProperties" : 1,
          "properties" : {
            "Include" : {
              "description" : "List of stack names that the hook is going to target",
              "type" : "array",
              "maxItems" : 50,
              "minItems" : 1,
              "uniqueItems" : True,
              "insertionOrder" : False,
              "items" : {
                "$ref" : "#/definitions/StackName"
              }
            },
            "Exclude" : {
              "description" : "List of stack names that the hook is going to be excluded from",
              "type" : "array",
              "maxItems" : 50,
              "minItems" : 1,
              "uniqueItems" : True,
              "insertionOrder" : False,
              "items" : {
                "$ref" : "#/definitions/StackName"
              }
            }
          }
        },
        "StackRoles" : {
          "description" : "List of stack roles that are performing the stack operations.",
          "type" : "object",
          "additionalProperties" : False,
          "minProperties" : 1,
          "properties" : {
            "Include" : {
              "description" : "List of stack roles that the hook is going to target",
              "type" : "array",
              "maxItems" : 50,
              "minItems" : 1,
              "uniqueItems" : True,
              "insertionOrder" : False,
              "items" : {
                "$ref" : "#/definitions/StackRole"
              }
            },
            "Exclude" : {
              "description" : "List of stack roles that the hook is going to be excluded from",
              "type" : "array",
              "maxItems" : 50,
              "minItems" : 1,
              "uniqueItems" : True,
              "insertionOrder" : False,
              "items" : {
                "$ref" : "#/definitions/StackRole"
              }
            }
          }
        }
      },
      "required" : [ "FilteringCriteria" ],
      "additionalProperties" : False
    },
    "Alias" : {
      "description" : "The typename alias for the hook.",
      "pattern" : "^(?!(?i)aws)[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$",
      "type" : "string"
    },
    "HookArn" : {
      "description" : "The Amazon Resource Name (ARN) of the activated hook",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/.+$",
      "type" : "string"
    },
    "ExecutionRole" : {
      "description" : "The execution role ARN assumed by Hooks to invoke Lambda.",
      "$ref" : "#/definitions/Role"
    }
  },
  "additionalProperties" : False,
  "required" : [ "LambdaFunction", "FailureMode", "Alias", "ExecutionRole", "TargetOperations", "HookStatus" ],
  "readOnlyProperties" : [ "/properties/HookArn" ],
  "createOnlyProperties" : [ "/properties/Alias" ],
  "primaryIdentifier" : [ "/properties/HookArn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudformation:ListTypes", "cloudformation:ActivateType", "cloudformation:BatchDescribeTypeConfigurations", "cloudformation:DescribeType", "cloudformation:SetTypeConfiguration", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "cloudformation:BatchDescribeTypeConfigurations", "cloudformation:DescribeType" ]
    },
    "update" : {
      "permissions" : [ "cloudformation:BatchDescribeTypeConfigurations", "cloudformation:DescribeType", "cloudformation:SetTypeConfiguration", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "cloudformation:BatchDescribeTypeConfigurations", "cloudformation:DeactivateType", "cloudformation:DescribeType", "cloudformation:SetTypeConfiguration" ]
    },
    "list" : {
      "permissions" : [ "cloudformation:ListTypes", "cloudformation:BatchDescribeTypeConfigurations", "cloudformation:DescribeType" ]
    }
  }
}
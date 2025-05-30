SCHEMA = {
  "typeName" : "AWS::CodePipeline::CustomActionType",
  "description" : "The AWS::CodePipeline::CustomActionType resource creates a custom action for activities that aren't included in the CodePipeline default actions, such as running an internally developed build process or a test suite. You can use these custom actions in the stage of a pipeline.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-codepipeline.git",
  "additionalProperties" : False,
  "properties" : {
    "Category" : {
      "description" : "The category of the custom action, such as a build action or a test action.",
      "type" : "string"
    },
    "ConfigurationProperties" : {
      "description" : "The configuration properties for the custom action.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/ConfigurationProperties"
      }
    },
    "InputArtifactDetails" : {
      "description" : "The details of the input artifact for the action, such as its commit ID.",
      "$ref" : "#/definitions/ArtifactDetails"
    },
    "OutputArtifactDetails" : {
      "description" : "The details of the output artifact of the action, such as its commit ID.",
      "$ref" : "#/definitions/ArtifactDetails"
    },
    "Provider" : {
      "description" : "The provider of the service used in the custom action, such as AWS CodeDeploy.",
      "type" : "string"
    },
    "Settings" : {
      "description" : "URLs that provide users information about this custom action.",
      "$ref" : "#/definitions/Settings"
    },
    "Tags" : {
      "description" : "Any tags assigned to the custom action.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Version" : {
      "description" : "The version identifier of the custom action.",
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "ConfigurationProperties" : {
      "additionalProperties" : False,
      "description" : "The configuration properties for the custom action.",
      "type" : "object",
      "properties" : {
        "Description" : {
          "description" : "The description of the action configuration property that is displayed to users. ",
          "type" : "string"
        },
        "Key" : {
          "description" : "Whether the configuration property is a key.",
          "type" : "boolean"
        },
        "Name" : {
          "description" : "The name of the action configuration property.",
          "type" : "string"
        },
        "Queryable" : {
          "description" : "Indicates that the property is used with PollForJobs. When creating a custom action, an action can have up to one queryable property. If it has one, that property must be both required and not secret.If you create a pipeline with a custom action type, and that custom action contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens. ",
          "type" : "boolean"
        },
        "Required" : {
          "description" : "Whether the configuration property is a required value.",
          "type" : "boolean"
        },
        "Secret" : {
          "description" : "Whether the configuration property is secret. Secrets are hidden from all calls except for GetJobDetails, GetThirdPartyJobDetails, PollForJobs, and PollForThirdPartyJobs.",
          "type" : "boolean"
        },
        "Type" : {
          "description" : "The type of the configuration property.",
          "type" : "string"
        }
      },
      "required" : [ "Key", "Name", "Required", "Secret" ]
    },
    "ArtifactDetails" : {
      "additionalProperties" : False,
      "description" : "Returns information about the details of an artifact.",
      "type" : "object",
      "properties" : {
        "MaximumCount" : {
          "description" : "The maximum number of artifacts allowed for the action type.",
          "type" : "integer"
        },
        "MinimumCount" : {
          "description" : "The minimum number of artifacts allowed for the action type.",
          "type" : "integer"
        }
      },
      "required" : [ "MaximumCount", "MinimumCount" ]
    },
    "Settings" : {
      "additionalProperties" : False,
      "description" : "Settings is a property of the AWS::CodePipeline::CustomActionType resource that provides URLs that users can access to view information about the CodePipeline custom action. ",
      "type" : "object",
      "properties" : {
        "EntityUrlTemplate" : {
          "description" : "The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system, such as the configuration page for an AWS CodeDeploy deployment group. This link is provided as part of the action display in the pipeline. ",
          "type" : "string"
        },
        "ExecutionUrlTemplate" : {
          "description" : "The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system, such as the console page for AWS CodeDeploy. This link is shown on the pipeline view page in the AWS CodePipeline console and provides a link to the execution entity of the external action. ",
          "type" : "string"
        },
        "RevisionUrlTemplate" : {
          "description" : "The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action. ",
          "type" : "string"
        },
        "ThirdPartyConfigurationUrl" : {
          "description" : "The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.",
          "type" : "string"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags"
  },
  "required" : [ "Category", "InputArtifactDetails", "OutputArtifactDetails", "Provider", "Version" ],
  "createOnlyProperties" : [ "/properties/Category", "/properties/ConfigurationProperties", "/properties/InputArtifactDetails", "/properties/OutputArtifactDetails", "/properties/Provider", "/properties/Settings", "/properties/Version" ],
  "writeOnlyProperties" : [ "/properties/ConfigurationProperties/*/Type" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Category", "/properties/Provider", "/properties/Version" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "codepipeline:CreateCustomActionType", "codepipeline:TagResource", "codepipeline:ListActionTypes" ]
    },
    "read" : {
      "permissions" : [ "codepipeline:ListActionTypes", "codepipeline:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "codepipeline:ListActionTypes", "codepipeline:TagResource", "codepipeline:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "codepipeline:DeleteCustomActionType", "codepipeline:ListActionTypes" ]
    },
    "list" : {
      "permissions" : [ "codepipeline:ListActionTypes" ]
    }
  }
}
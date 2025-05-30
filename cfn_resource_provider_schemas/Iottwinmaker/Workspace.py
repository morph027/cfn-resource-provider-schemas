SCHEMA = {
  "typeName" : "AWS::IoTTwinMaker::Workspace",
  "description" : "Resource schema for AWS::IoTTwinMaker::Workspace",
  "definitions" : {
    "DateTimeFormat" : {
      "type" : "string",
      "format" : "date-time"
    }
  },
  "properties" : {
    "WorkspaceId" : {
      "description" : "The ID of the workspace.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[a-zA-Z_0-9][a-zA-Z_\\-0-9]*[a-zA-Z0-9]+"
    },
    "Arn" : {
      "description" : "The ARN of the workspace.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\\/a-zA-Z0-9_\\-\\.:]+"
    },
    "Description" : {
      "description" : "The description of the workspace.",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 512
    },
    "Role" : {
      "description" : "The ARN of the execution role associated with the workspace.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*"
    },
    "S3Location" : {
      "description" : "The ARN of the S3 bucket where resources associated with the workspace are stored.",
      "type" : "string"
    },
    "CreationDateTime" : {
      "description" : "The date and time when the workspace was created.",
      "$ref" : "#/definitions/DateTimeFormat"
    },
    "UpdateDateTime" : {
      "description" : "The date and time of the current update.",
      "$ref" : "#/definitions/DateTimeFormat"
    },
    "Tags" : {
      "type" : "object",
      "description" : "A map of key-value pairs to associate with a resource.",
      "patternProperties" : {
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "maxProperties" : 50,
      "additionalProperties" : False
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iottwinmaker:TagResource", "iottwinmaker:UntagResource", "iottwinmaker:ListTagsForResource" ]
  },
  "required" : [ "WorkspaceId", "Role", "S3Location" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationDateTime", "/properties/UpdateDateTime" ],
  "createOnlyProperties" : [ "/properties/WorkspaceId" ],
  "primaryIdentifier" : [ "/properties/WorkspaceId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "iottwinmaker:CreateWorkspace", "iottwinmaker:GetWorkspace", "iottwinmaker:ListTagsForResource", "iottwinmaker:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iottwinmaker:GetWorkspace", "iottwinmaker:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iottwinmaker:GetWorkspace", "iottwinmaker:ListTagsForResource", "iottwinmaker:TagResource", "iottwinmaker:UntagResource", "iottwinmaker:UpdateWorkspace" ]
    },
    "delete" : {
      "permissions" : [ "iottwinmaker:DeleteWorkspace", "iottwinmaker:GetWorkspace" ]
    },
    "list" : {
      "permissions" : [ "iottwinmaker:GetWorkspace", "iottwinmaker:ListTagsForResource", "iottwinmaker:ListWorkspaces" ]
    }
  }
}
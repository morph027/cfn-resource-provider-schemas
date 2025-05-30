SCHEMA = {
  "typeName" : "AWS::IoTTwinMaker::SyncJob",
  "description" : "Resource schema for AWS::IoTTwinMaker::SyncJob",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iottwinmaker",
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
    "SyncSource" : {
      "description" : "The source of the SyncJob.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "SyncRole" : {
      "description" : "The IAM Role that execute SyncJob.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "arn:((aws)|(aws-cn)|(aws-us-gov)):iam::[0-9]{12}:role/.*"
    },
    "CreationDateTime" : {
      "description" : "The date and time when the sync job was created.",
      "$ref" : "#/definitions/DateTimeFormat"
    },
    "UpdateDateTime" : {
      "description" : "The date and time when the sync job was updated.",
      "$ref" : "#/definitions/DateTimeFormat"
    },
    "Arn" : {
      "description" : "The ARN of the SyncJob.",
      "type" : "string",
      "minLength" : 20,
      "maxLength" : 2048,
      "pattern" : "arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\\/a-zA-Z0-9_\\-\\.:]+"
    },
    "State" : {
      "description" : "The state of SyncJob.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "[a-zA-Z_\\-0-9]+"
    },
    "Tags" : {
      "type" : "object",
      "description" : "A key-value pair to associate with a resource.",
      "patternProperties" : {
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    }
  },
  "additionalProperties" : False,
  "required" : [ "WorkspaceId", "SyncSource", "SyncRole" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationDateTime", "/properties/UpdateDateTime", "/properties/State" ],
  "createOnlyProperties" : [ "/properties/WorkspaceId", "/properties/SyncSource", "/properties/SyncRole", "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/WorkspaceId", "/properties/SyncSource" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iottwinmaker:TagResource", "iottwinmaker:UntagResource", "iottwinmaker:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:PassRole", "iottwinmaker:CreateSyncJob", "iottwinmaker:GetSyncJob", "iottwinmaker:GetWorkspace", "iottwinmaker:ListTagsForResource", "iottwinmaker:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iottwinmaker:GetSyncJob", "iottwinmaker:GetWorkspace", "iottwinmaker:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "iottwinmaker:DeleteSyncJob", "iottwinmaker:GetSyncJob", "iottwinmaker:GetWorkspace" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "WorkspaceId" : {
            "type" : "string",
            "$ref" : "resource-schema.json#/properties/WorkspaceId"
          }
        },
        "required" : [ "WorkspaceId" ]
      },
      "permissions" : [ "iottwinmaker:GetWorkspace", "iottwinmaker:ListSyncJobs", "iottwinmaker:ListTagsForResource" ]
    }
  },
  "replacementStrategy" : "delete_then_create"
}
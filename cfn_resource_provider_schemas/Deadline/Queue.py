SCHEMA = {
  "typeName" : "AWS::Deadline::Queue",
  "description" : "Definition of AWS::Deadline::Queue Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-deadline",
  "definitions" : {
    "DefaultQueueBudgetAction" : {
      "type" : "string",
      "default" : "NONE",
      "enum" : [ "NONE", "STOP_SCHEDULING_AND_COMPLETE_TASKS", "STOP_SCHEDULING_AND_CANCEL_TASKS" ]
    },
    "JobAttachmentSettings" : {
      "type" : "object",
      "properties" : {
        "S3BucketName" : {
          "type" : "string",
          "maxLength" : 63,
          "minLength" : 3,
          "pattern" : "(?!^(\\d+\\.)+\\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)"
        },
        "RootPrefix" : {
          "type" : "string",
          "maxLength" : 63,
          "minLength" : 1
        }
      },
      "required" : [ "RootPrefix", "S3BucketName" ],
      "additionalProperties" : False
    },
    "JobRunAsUser" : {
      "type" : "object",
      "properties" : {
        "Posix" : {
          "$ref" : "#/definitions/PosixUser"
        },
        "Windows" : {
          "$ref" : "#/definitions/WindowsUser"
        },
        "RunAs" : {
          "$ref" : "#/definitions/RunAs"
        }
      },
      "required" : [ "RunAs" ],
      "additionalProperties" : False
    },
    "PosixUser" : {
      "type" : "object",
      "properties" : {
        "User" : {
          "type" : "string",
          "maxLength" : 31,
          "minLength" : 0,
          "pattern" : "^(?:[a-z][a-z0-9-]{0,30})?$"
        },
        "Group" : {
          "type" : "string",
          "maxLength" : 31,
          "minLength" : 0,
          "pattern" : "^(?:[a-z][a-z0-9-]{0,30})?$"
        }
      },
      "required" : [ "Group", "User" ],
      "additionalProperties" : False
    },
    "RunAs" : {
      "type" : "string",
      "enum" : [ "QUEUE_CONFIGURED_USER", "WORKER_AGENT_USER" ]
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "WindowsUser" : {
      "type" : "object",
      "properties" : {
        "User" : {
          "type" : "string",
          "maxLength" : 111,
          "minLength" : 0,
          "pattern" : "^[^\"'/\\[\\]:;|=,+*?<>\\s]*$"
        },
        "PasswordArn" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 20,
          "pattern" : "^arn:(aws[a-zA-Z-]*):secretsmanager:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\\d{1}:\\d{12}:secret:[a-zA-Z0-9-/_+=.@]{1,2028}$"
        }
      },
      "required" : [ "PasswordArn", "User" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "AllowedStorageProfileIds" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "pattern" : "^sp-[0-9a-f]{32}$"
      },
      "maxItems" : 20,
      "minItems" : 0,
      "uniqueItems" : True
    },
    "DefaultBudgetAction" : {
      "$ref" : "#/definitions/DefaultQueueBudgetAction"
    },
    "Description" : {
      "type" : "string",
      "default" : "",
      "maxLength" : 100,
      "minLength" : 0
    },
    "DisplayName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1
    },
    "FarmId" : {
      "type" : "string",
      "pattern" : "^farm-[0-9a-f]{32}$"
    },
    "JobAttachmentSettings" : {
      "$ref" : "#/definitions/JobAttachmentSettings"
    },
    "JobRunAsUser" : {
      "$ref" : "#/definitions/JobRunAsUser"
    },
    "QueueId" : {
      "type" : "string",
      "pattern" : "^queue-[0-9a-f]{32}$"
    },
    "RequiredFileSystemLocationNames" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "maxLength" : 64,
        "minLength" : 1,
        "pattern" : "^[0-9A-Za-z ]*$"
      },
      "maxItems" : 20,
      "minItems" : 0,
      "uniqueItems" : True
    },
    "RoleArn" : {
      "type" : "string",
      "pattern" : "^arn:(aws[a-zA-Z-]*):iam::\\d{12}:role(/[!-.0-~]+)*/[\\w+=,.@-]+$"
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:*"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "insertionOrder" : False,
      "uniqueItems" : True
    }
  },
  "required" : [ "DisplayName", "FarmId" ],
  "readOnlyProperties" : [ "/properties/QueueId", "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/FarmId" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "deadline:TagResource", "deadline:UntagResource", "deadline:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:CreateQueue", "deadline:GetQueue", "iam:PassRole", "identitystore:ListGroupMembershipsForMember", "logs:CreateLogGroup", "s3:ListBucket", "deadline:TagResource", "deadline:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetQueue", "identitystore:ListGroupMembershipsForMember", "deadline:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "deadline:UpdateQueue", "deadline:GetQueue", "iam:PassRole", "identitystore:ListGroupMembershipsForMember", "logs:CreateLogGroup", "s3:ListBucket", "deadline:TagResource", "deadline:UntagResource", "deadline:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "deadline:DeleteQueue", "deadline:GetQueue", "identitystore:ListGroupMembershipsForMember" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "FarmId" : {
            "$ref" : "resource-schema.json#/properties/FarmId"
          }
        },
        "required" : [ "FarmId" ]
      },
      "permissions" : [ "deadline:ListQueues", "identitystore:DescribeGroup", "identitystore:DescribeUser", "identitystore:ListGroupMembershipsForMember" ]
    }
  },
  "additionalProperties" : False
}
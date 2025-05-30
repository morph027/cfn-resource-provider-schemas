SCHEMA = {
  "typeName" : "AWS::QuickSight::Folder",
  "description" : "Definition of the AWS::QuickSight::Folder Resource Type.",
  "definitions" : {
    "FolderType" : {
      "type" : "string",
      "enum" : [ "SHARED", "RESTRICTED" ]
    },
    "ResourcePermission" : {
      "type" : "object",
      "description" : "<p>Permission for the resource.</p>",
      "properties" : {
        "Principal" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "<p>The Amazon Resource Name (ARN) of the principal. This can be one of the\n            following:</p>\n         <ul>\n            <li>\n               <p>The ARN of an Amazon QuickSight user or group associated with a data source or dataset. (This is common.)</p>\n            </li>\n            <li>\n               <p>The ARN of an Amazon QuickSight user, group, or namespace associated with an analysis, dashboard, template, or theme. (This is common.)</p>\n            </li>\n            <li>\n               <p>The ARN of an Amazon Web Services account root: This is an IAM ARN rather than a QuickSight\n                    ARN. Use this option only to share resources (templates) across Amazon Web Services accounts.\n                    (This is less common.) </p>\n            </li>\n         </ul>",
          "pattern" : "^arn:.*"
        },
        "Actions" : {
          "type" : "array",
          "items" : {
            "type" : "string"
          },
          "maxItems" : 20,
          "minItems" : 1,
          "description" : "<p>The IAM action to grant or revoke permissions on.</p>",
          "insertionOrder" : False
        }
      },
      "required" : [ "Actions", "Principal" ],
      "additionalProperties" : False
    },
    "SharingModel" : {
      "type" : "string",
      "enum" : [ "ACCOUNT", "NAMESPACE" ]
    },
    "Tag" : {
      "type" : "object",
      "description" : "<p>The key or keys of the key-value pairs for the resource tag or tags assigned to the\n            resource.</p>",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "<p>Tag key.</p>"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "<p>Tag value.</p>"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "<p>The Amazon Resource Name (ARN) for the folder.</p>",
      "pattern" : "^arn:.*"
    },
    "AwsAccountId" : {
      "type" : "string",
      "maxLength" : 12,
      "minLength" : 12,
      "pattern" : "^[0-9]{12}$"
    },
    "CreatedTime" : {
      "type" : "string",
      "description" : "<p>The time that the folder was created.</p>",
      "format" : "date-time"
    },
    "FolderId" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "pattern" : "^[\\w\\-]+$"
    },
    "FolderType" : {
      "$ref" : "#/definitions/FolderType"
    },
    "LastUpdatedTime" : {
      "type" : "string",
      "description" : "<p>The time that the folder was last updated.</p>",
      "format" : "date-time"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 1
    },
    "ParentFolderArn" : {
      "type" : "string"
    },
    "Permissions" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ResourcePermission"
      },
      "maxItems" : 64,
      "minItems" : 1,
      "insertionOrder" : False
    },
    "SharingModel" : {
      "$ref" : "#/definitions/SharingModel"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 1,
      "insertionOrder" : False
    }
  },
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreatedTime", "/properties/LastUpdatedTime" ],
  "writeOnlyProperties" : [ "/properties/ParentFolderArn" ],
  "createOnlyProperties" : [ "/properties/ParentFolderArn", "/properties/SharingModel", "/properties/FolderType", "/properties/FolderId", "/properties/AwsAccountId" ],
  "primaryIdentifier" : [ "/properties/AwsAccountId", "/properties/FolderId" ],
  "handlers" : {
    "read" : {
      "permissions" : [ "quicksight:DescribeFolder", "quicksight:DescribeFolderPermissions", "quicksight:ListTagsForResource" ]
    },
    "create" : {
      "permissions" : [ "quicksight:CreateFolder", "quicksight:DescribeFolder", "quicksight:UpdateFolderPermissions", "quicksight:DescribeFolderPermissions", "quicksight:TagResource", "quicksight:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "quicksight:DescribeFolder", "quicksight:UpdateFolder", "quicksight:DescribeFolderPermissions", "quicksight:UpdateFolderPermissions", "quicksight:ListTagsForResource", "quicksight:TagResource", "quicksight:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "quicksight:DeleteFolder" ]
    },
    "list" : {
      "permissions" : [ "quicksight:ListFolders" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "quicksight:TagResource", "quicksight:UntagResource", "quicksight:ListTagsForResource" ]
  }
}
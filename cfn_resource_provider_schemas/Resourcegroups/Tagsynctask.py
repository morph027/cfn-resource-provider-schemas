SCHEMA = {
  "typeName" : "AWS::ResourceGroups::TagSyncTask",
  "description" : "Schema for ResourceGroups::TagSyncTask",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "Group" : {
      "description" : "The Amazon resource name (ARN) or name of the application group for which you want to create a tag-sync task",
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 12,
      "pattern" : "([a-zA-Z0-9_\\\\.-]{1,150}/[a-z0-9]{26})|(arn:aws(-[a-z]+)*:resource-groups(-(test|beta|gamma))?:[a-z]{2}(-[a-z]+)+-\\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\\\\.-]{1,150}/[a-z0-9]{26})"
    },
    "GroupArn" : {
      "description" : "The Amazon resource name (ARN) of the ApplicationGroup for which the TagSyncTask is created",
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 12,
      "pattern" : "arn:aws(-[a-z]+)*:resource-groups(-(test|beta|gamma))?:[a-z]{2}(-[a-z]+)+-\\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\\.-]{1,150}/[a-z0-9]{26}"
    },
    "GroupName" : {
      "description" : "The Name of the application group for which the TagSyncTask is created",
      "type" : "string",
      "maxLength" : 300,
      "minLength" : 1,
      "pattern" : "[a-zA-Z0-9_\\.-]{1,150}/[a-z0-9]{26}"
    },
    "TaskArn" : {
      "description" : "The ARN of the TagSyncTask resource",
      "type" : "string",
      "maxLength" : 1600,
      "minLength" : 12,
      "pattern" : "arn:aws(-[a-z]+)*:resource-groups(-(test|beta|gamma))?:[a-z]{2}(-[a-z]+)+-\\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\\.-]{1,150}/[a-z0-9]{26}/tag-sync-task/[a-z0-9]{26}"
    },
    "TagKey" : {
      "description" : "The tag key. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application.",
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 1,
      "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
    },
    "TagValue" : {
      "description" : "The tag value. Resources tagged with this tag key-value pair will be added to the application. If a resource with this tag is later untagged, the tag-sync task removes the resource from the application.",
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0,
      "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
    },
    "RoleArn" : {
      "description" : "The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.",
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "arn:(aws[a-zA-Z-]*)?:iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+"
    },
    "Status" : {
      "description" : "The status of the TagSyncTask",
      "type" : "string",
      "enum" : [ "ACTIVE", "ERROR" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "Group", "TagKey", "TagValue", "RoleArn" ],
  "createOnlyProperties" : [ "/properties/Group", "/properties/TagKey", "/properties/TagValue", "/properties/RoleArn" ],
  "readOnlyProperties" : [ "/properties/TaskArn", "/properties/Status", "/properties/GroupName", "/properties/GroupArn" ],
  "primaryIdentifier" : [ "/properties/TaskArn" ],
  "propertyTransform" : {
    "/properties/Group" : "$split(Group, \"/\")[1] & \"/\" & $split(Group, \"/\")[2] $OR Group"
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "resource-groups:StartTagSyncTask", "resource-groups:CreateGroup", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "resource-groups:GetTagSyncTask" ]
    },
    "delete" : {
      "permissions" : [ "resource-groups:CancelTagSyncTask", "resource-groups:DeleteGroup" ]
    },
    "list" : {
      "permissions" : [ "resource-groups:ListTagSyncTasks" ]
    }
  }
}
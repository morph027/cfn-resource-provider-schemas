SCHEMA = {
  "typeName" : "AWS::IoTSiteWise::Dashboard",
  "description" : "Resource schema for AWS::IoTSiteWise::Dashboard",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-iotsitewise.git",
  "definitions" : {
    "Tag" : {
      "description" : "To add or update tag, provide both key and value. To delete tag, provide only tag key to be deleted",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "ProjectId" : {
      "description" : "The ID of the project in which to create the dashboard.",
      "type" : "string"
    },
    "DashboardId" : {
      "description" : "The ID of the dashboard.",
      "type" : "string"
    },
    "DashboardName" : {
      "description" : "A friendly name for the dashboard.",
      "type" : "string"
    },
    "DashboardDescription" : {
      "description" : "A description for the dashboard.",
      "type" : "string"
    },
    "DashboardDefinition" : {
      "description" : "The dashboard definition specified in a JSON literal.",
      "type" : "string"
    },
    "DashboardArn" : {
      "description" : "The ARN of the dashboard.",
      "type" : "string"
    },
    "Tags" : {
      "description" : "A list of key-value pairs that contain metadata for the dashboard.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotsitewise:TagResource", "iotsitewise:UntagResource", "iotsitewise:ListTagsForResource" ]
  },
  "required" : [ "DashboardDefinition", "DashboardDescription", "DashboardName" ],
  "readOnlyProperties" : [ "/properties/DashboardArn", "/properties/DashboardId" ],
  "createOnlyProperties" : [ "/properties/ProjectId" ],
  "primaryIdentifier" : [ "/properties/DashboardId" ],
  "additionalIdentifiers" : [ [ "/properties/DashboardArn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotsitewise:CreateDashboard", "iotsitewise:DescribeDashboard", "iotsitewise:ListTagsForResource", "iotsitewise:TagResource", "iotsitewise:DescribeAsset", "iotsitewise:DescribeAssetModel", "iotsitewise:ListAssetModelProperties", "iotsitewise:ListAssetModelCompositeModels" ]
    },
    "read" : {
      "permissions" : [ "iotsitewise:DescribeDashboard", "iotsitewise:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotsitewise:DescribeDashboard", "iotsitewise:UpdateDashboard", "iotsitewise:TagResource", "iotsitewise:UntagResource", "iotsitewise:ListTagsForResource", "iotsitewise:DescribeAsset", "iotsitewise:DescribeAssetModel", "iotsitewise:ListAssetModelProperties", "iotsitewise:ListAssetModelCompositeModels" ]
    },
    "delete" : {
      "permissions" : [ "iotsitewise:DescribeDashboard", "iotsitewise:DeleteDashboard" ]
    },
    "list" : {
      "permissions" : [ "iotsitewise:ListDashboards", "iotsitewise:ListPortals", "iotsitewise:ListProjects", "iotsitewise:ListTagsForResource" ]
    }
  }
}
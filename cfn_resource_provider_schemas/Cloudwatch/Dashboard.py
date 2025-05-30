SCHEMA = {
  "typeName" : "AWS::CloudWatch::Dashboard",
  "description" : "Resource Type definition for AWS::CloudWatch::Dashboard",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudwatch",
  "additionalProperties" : False,
  "properties" : {
    "DashboardName" : {
      "type" : "string",
      "description" : "The name of the dashboard. The name must be between 1 and 255 characters. If you do not specify a name, one will be generated automatically."
    },
    "DashboardBody" : {
      "type" : "string",
      "description" : "The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "DashboardBody" ],
  "createOnlyProperties" : [ "/properties/DashboardName" ],
  "primaryIdentifier" : [ "/properties/DashboardName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudwatch:PutDashboard", "cloudwatch:GetDashboard" ]
    },
    "read" : {
      "permissions" : [ "cloudwatch:GetDashboard" ]
    },
    "update" : {
      "permissions" : [ "cloudwatch:PutDashboard" ]
    },
    "delete" : {
      "permissions" : [ "cloudwatch:DeleteDashboards", "cloudwatch:GetDashboard" ]
    },
    "list" : {
      "permissions" : [ "cloudwatch:ListDashboards" ]
    }
  }
}
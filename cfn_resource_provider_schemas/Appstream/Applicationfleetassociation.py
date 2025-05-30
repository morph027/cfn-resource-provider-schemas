SCHEMA = {
  "typeName" : "AWS::AppStream::ApplicationFleetAssociation",
  "description" : "Resource Type definition for AWS::AppStream::ApplicationFleetAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-appstream.git",
  "definitions" : {
    "Arn" : {
      "type" : "string"
    }
  },
  "properties" : {
    "FleetName" : {
      "type" : "string"
    },
    "ApplicationArn" : {
      "$ref" : "#/definitions/Arn"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "FleetName", "ApplicationArn" ],
  "createOnlyProperties" : [ "/properties/FleetName", "/properties/ApplicationArn" ],
  "primaryIdentifier" : [ "/properties/FleetName", "/properties/ApplicationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appstream:AssociateApplicationFleet", "appstream:DescribeApplicationFleetAssociations" ]
    },
    "read" : {
      "permissions" : [ "appstream:DescribeApplicationFleetAssociations" ]
    },
    "delete" : {
      "permissions" : [ "appstream:DisassociateApplicationFleet", "appstream:DescribeApplicationFleetAssociations" ]
    }
  }
}
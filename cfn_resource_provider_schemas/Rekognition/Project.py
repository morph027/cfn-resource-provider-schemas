SCHEMA = {
  "typeName" : "AWS::Rekognition::Project",
  "description" : "The AWS::Rekognition::Project type creates an Amazon Rekognition CustomLabels Project. A project is a grouping of the resources needed to create and manage Dataset and ProjectVersions.",
  "sourceUrl" : "https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/cp-manage-project.html",
  "definitions" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 2048,
      "pattern" : "(^arn:[a-z\\d-]+:rekognition:[a-z\\d-]+:\\d{12}:project/[a-zA-Z0-9_.\\-]{1,255}/[0-9]+$)"
    },
    "ProjectName" : {
      "description" : "The name of the project",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255,
      "pattern" : "[a-zA-Z0-9][a-zA-Z0-9_\\-]*"
    }
  },
  "properties" : {
    "Arn" : {
      "$ref" : "#/definitions/Arn"
    },
    "ProjectName" : {
      "$ref" : "#/definitions/ProjectName"
    }
  },
  "additionalProperties" : False,
  "required" : [ "ProjectName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/ProjectName" ],
  "primaryIdentifier" : [ "/properties/ProjectName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "rekognition:CreateProject" ],
      "timeoutInMinutes" : 15
    },
    "read" : {
      "permissions" : [ "rekognition:DescribeProjects" ],
      "timeoutInMinutes" : 15
    },
    "update" : {
      "permissions" : [ ],
      "timeoutInMinutes" : 15
    },
    "delete" : {
      "permissions" : [ "rekognition:DescribeProjects", "rekognition:DeleteProject" ],
      "timeoutInMinutes" : 15
    },
    "list" : {
      "permissions" : [ "rekognition:DescribeProjects" ],
      "timeoutInMinutes" : 15
    }
  }
}